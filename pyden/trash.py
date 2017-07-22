"""
File: trash.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/bachya
"""

from six.moves.urllib.parse import quote_plus

import arrow
import geocoder
import ics

import pyden.api as api
import pyden.exceptions as exceptions

BASE_URL = 'https://recollect.net/api'
LOOKUP_URL = 'lookup/{0},{1}.json?service={2}&address={3}&locale=en-US&' \
        'postal_code={4}&street_number={5}&street_name={6}&subpremise=&' \
        'locality={7}&territory={8}&country={9}'
SCHEDULE_URL = 'places/{0}/services/{1}/events.en-US.ics'
SERVICE_ID = 248


class Trash(api.BaseAPI):
    """ A class to handle requesting trash/recycling info """

    def __init__(self, coordinates, **kwargs):
        """ Initialize! """
        super(Trash, self).__init__(BASE_URL, **kwargs)
        self.place_id = self._get_place_id(coordinates)

    def _get_place_id(self, coordinates):
        """ Figure out the place ID based on coordinates """
        latitude, longitude = coordinates
        coder = geocoder.google([latitude, longitude], method='reverse')

        if coder.status == 'OK':
            street_number = coder.housenumber
            street_name = coder.street_long
            locality = coder.city
            territory = coder.state
            postal_code = coder.postal
            country = coder.country
            address = '{0} {1}, {2}, {3} {4} {5}'.format(
                street_number, street_name, locality, territory, postal_code,
                country)
            encoded_address = quote_plus(address)

            resp = self.get(
                LOOKUP_URL.format(latitude, longitude, SERVICE_ID,
                                  encoded_address, postal_code, street_number,
                                  street_name, locality, territory, country))
            try:
                return resp.json()['place']['id']
            except KeyError:
                raise exceptions.GeocodingError(
                    'Unable to get a valid schedule for address: {0}'.format(
                        address))
        else:
            raise exceptions.GeocodingError(
                'Unable to get an address for coordinates: {0}'.format(
                    coordinates))

    def schedule(self):
        """ Return the schedule from the current date forward """
        events = {}
        resp = self.get(SCHEDULE_URL.format(self.place_id, SERVICE_ID))
        for event in ics.Calendar(resp.text).events:
            if arrow.now().date() <= event.begin.date():
                event_title = event.name.lower()
                events[event.begin.format('YYYY-MM-DD')] = {
                    'compost': 'compost' in event_title,
                    'extra_trash': 'extra trash' in event_title,
                    'recycling': 'recycling' in event_title,
                    'trash': 'trash' in event_title
                }

        return events
