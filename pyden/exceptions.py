"""
File: exceptions.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/bachya/pyden
"""


class GeocodingError(Exception):
    """ Unable to geocode a set of coordinates """
    pass


class HTTPError(Exception):
    """ Some sort of HTTP error occurred """
    pass
