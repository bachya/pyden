"""
File: api.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/bachya
"""

import requests

import pyden.exceptions


class BaseAPI(object):
    """ Class that represents a base API request """

    def __init__(self, base_url, session=None):
        """ Initialize ! """

        self.base_url = base_url
        self.session = session

    def request(self, method_type, url, **kwargs):
        """ A generic request to the city's site/resources """

        full_url = '{0}/{1}'.format(self.base_url, url)
        method = getattr(self.session
                         if self.session else requests, method_type)
        resp = method(full_url, **kwargs)

        # I don't think it's good form to make end users of pyden have
        # to explicitly catch exceptions from a sub-library, so here, I
        # wrap the Requests HTTPError in my own:
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as exc_info:
            raise pyden.exceptions.HTTPError(str(exc_info))

        return resp

    def get(self, url, **kwargs):
        """ Generic GET request """
        return self.request('get', url, **kwargs)
