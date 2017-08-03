"""
File: trash.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/bachya
"""

from collections import OrderedDict

import icalendar
import maya
from cachecontrol import CacheControl
from cachecontrol.heuristics import ExpiresAfter
from requests import Session

import pyden.api as api
import pyden.exceptions as exceptions
import pyden.util as util

BASE_URL = 'https://recollect.net/api'
DEFAULT_TIMEZONE = 'America/Denver'
LOOKUP_URL = 'lookup/{0},{1}.json?service={2}&address={3}&locale=en-US&' \
        'postal_code={4}&street_number={5}&street_name={6}&subpremise=&' \
        'locality={7}&territory={8}&country={9}'
SCHEDULE_CACHE_TIMING = 60 * 60 * 24 * 7 * 4 * 1
SCHEDULE_URL = 'places/{0}/services/{1}/events.en-US.ics'
SERVICE_ID = 248


class TrashClient(api.BaseAPI):
    """ A class to handle requesting trash/recycling info """

    def __init__(self,
                 place_id,
                 cache=True,
                 time_to_cache=SCHEDULE_CACHE_TIMING,
                 **kwargs):
        """ Initialize! """
        if cache:
            session = CacheControl(
                Session(), heuristic=ExpiresAfter(seconds=time_to_cache))
        else:
            session = None

        super(TrashClient, self).__init__(BASE_URL, session, **kwargs)
        self._place_id = place_id

    def __eq__(self, other):
        """ Defines how this object should be compared to others """
        return self.__dict__ == other.__dict__

    @property
    def place_id(self):
        """ Recollect place ID getter """

        return self._place_id

    @place_id.setter
    def place_id(self, value):
        """ Recollect place ID setter """
        self._place_id = value

    @classmethod
    def from_coordinates(cls, latitude, longitude, **kwargs):
        """ Create a TrashClient based on a passed-in place_id """
        from urllib.parse import quote_plus

        klass = cls(None, **kwargs)

        coder = util.get_coder_from_coords(latitude, longitude)
        address = '{0} {1}, {2}, {3} {4} {5}'.format(
            coder.housenumber, coder.street_long, coder.city, coder.state,
            coder.postal, coder.country)
        encoded_address = quote_plus(address)

        resp = klass.get(
            LOOKUP_URL.format(latitude, longitude, SERVICE_ID, encoded_address,
                              coder.postal, coder.housenumber,
                              coder.street_long, coder.city, coder.state,
                              coder.country))
        try:
            klass.place_id = resp.json()['place']['id']
            return klass
        except KeyError:
            raise exceptions.GeocodingError(
                'Unable to get a valid schedule for address: {0}'.format(
                    address))

    @classmethod
    def from_place_id(cls, place_id, **kwargs):
        """ Create a TrashClient based on a passed-in place_id """
        return cls(place_id, **kwargs)

    def next_pickup(self, pickup_type):
        """ Figures out the next pickup date for a particular type """
        schedule = self.schedule()
        for date, pickups in schedule.items():
            try:
                if pickups[pickup_type] is True:
                    return date
            except KeyError:
                raise exceptions.TrashTypeError(
                    'Could not find date for pickup type: {}'.format(
                        pickup_type)) from None

    def schedule(self):
        """ Return the schedule from the current date forward """
        events = OrderedDict()

        try:
            resp = self.get(SCHEDULE_URL.format(self.place_id, SERVICE_ID))
            calendar = icalendar.Calendar.from_ical(resp.text)
            for event in calendar.walk('vevent'):
                raw_date = str(event.decoded('dtstart'))
                event_date = maya.when(raw_date, timezone=DEFAULT_TIMEZONE)
                if maya.now() <= event_date:
                    event_title = event.get('summary').lower()
                    events[raw_date] = {
                        'compost': 'compost' in event_title,
                        'extra_trash': 'extra trash' in event_title,
                        'recycling': 'recycling' in event_title,
                        'trash': 'trash' in event_title
                    }

            return events
        except Exception:
            raise ValueError('Unable to get trash schedule for place ID: {}'.
                             format(self.place_id)) from None
