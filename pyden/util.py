"""
File: util.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/pyden
"""

import geocoder

import pyden.exceptions as exceptions

def get_coder_from_coords(latitude, longitude):
    """ Lookup an geocoder based on latitude and longitude """
    coder = geocoder.google([latitude, longitude], method='reverse')
    if coder.status == 'OK':
        return coder

    raise exceptions.GeocodingError(
        'Unable to get an address for coordinates: {0}, {1}'.format(
            latitude, longitude))
