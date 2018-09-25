"""Define an object to deal with trash/recycling data."""
import asyncio
from collections import OrderedDict
from datetime import datetime
from enum import Enum
from typing import Awaitable, Callable, Dict, Union
from urllib.parse import quote_plus

from aiocache import cached

import pytz as tz
from ics import Calendar
from geocoder import google
from geocoder.google_reverse import GoogleReverse

from .errors import PydenError

CALENDAR_URL = 'https://recollect.a.ssl.fastly.net/api/places/{0}/services/' \
    '{1}/events.en-US.ics'
PLACE_LOOKUP_URL = 'https://recollect.net/api/lookup/{0},{1}.json?' \
    'service={2}&address={3}&locale={4}&postal_code={5}&' \
    'street_number={6}&street_name={7}&subpremise=&locality={8}&' \
    'territory={9}&country={10}'

DEFAULT_CACHE_SECONDS = 60 * 60 * 24 * 7 * 4 * 1
DEFAULT_LOCALE = 'en-US'
DEFAULT_SERVICE_ID = 248
DEFAULT_TIMEZONE = tz.timezone('America/Denver')


def raise_on_invalid_place(func: Callable) -> Callable:
    """Raise an exception when a place ID hasn't been set."""
    async def decorator(self, *args: list, **kwargs: dict) -> Awaitable:
        """Decorate."""
        if not self.place_id:
            raise PydenError('No Recollect place ID given')
        return await func(self, *args, **kwargs)

    return decorator


class Trash:
    """Define the client."""

    class PickupTypes(Enum):
        """Define an enum for presence states."""

        compost = 'Compost'
        extra_trash = 'Extra Trash'
        recycling = 'Recycling'
        trash = 'Trash'

    def __init__(
            self, request: Callable[..., Awaitable],
            loop: asyncio.AbstractEventLoop) -> None:
        """Initialize."""
        self._loop = loop
        self._request = request
        self.place_id = None

    @staticmethod
    def _get_geo_data(
            latitude: float, longitude: float,
            google_api_key: str) -> GoogleReverse:
        """Return geo data from a set of coordinates."""
        return google([latitude, longitude],
                      key=google_api_key,
                      method='reverse')

    async def init_from_coords(
            self, latitude: float, longitude: float,
            google_api_key: str) -> None:
        """Initialize the client from a set of coordinates."""
        geo = await self._loop.run_in_executor(
            None, self._get_geo_data, latitude, longitude, google_api_key)
        lookup = await self._request(
            'get',
            PLACE_LOOKUP_URL.format(
                latitude, longitude, DEFAULT_SERVICE_ID,
                quote_plus(
                    '{0} {1}, {2}, {3}, {4}'.format(
                        geo.housenumber, geo.street_long, geo.city,
                        geo.state_long, geo.country_long)), DEFAULT_LOCALE,
                geo.postal, geo.housenumber, quote_plus(geo.street_long),
                quote_plus(geo.city), quote_plus(geo.state_long),
                quote_plus(geo.country_long)))

        try:
            self.place_id = lookup['place']['id']
        except (KeyError, TypeError):
            raise PydenError('Unable to find Recollect place ID')

    @raise_on_invalid_place
    async def next_pickup(self, pickup_type: Enum) -> Union[None, datetime]:
        """Figure out the next pickup date for a particular type."""
        schedule = await self.upcoming_schedule()
        for date, pickups in schedule.items():
            if pickups[pickup_type]:
                return date
        return None

    @cached(ttl=DEFAULT_CACHE_SECONDS)
    @raise_on_invalid_place
    async def upcoming_schedule(self) -> Dict[datetime, Dict[Enum, bool]]:
        """Get the upcoming trash/recycling schedule for the location."""
        events = OrderedDict()  # type: dict

        resp = await self._request(
            'get',
            CALENDAR_URL.format(self.place_id, DEFAULT_SERVICE_ID),
            kind='text')
        calendar = Calendar(resp)

        now = DEFAULT_TIMEZONE.localize(datetime.now())
        for event in calendar.events:
            pickup_date = event.begin.datetime.replace(tzinfo=DEFAULT_TIMEZONE)
            if now <= pickup_date:
                title = event.name.lower()
                if 'trash' in title:
                    events[pickup_date] = {
                        self.PickupTypes.compost: 'compost' in title,
                        self.PickupTypes.extra_trash: 'extra trash' in title,
                        self.PickupTypes.recycling: 'recycl' in title,
                        self.PickupTypes.trash: 'trash' in title
                    }
        return OrderedDict(sorted(events.items(), reverse=False))
