"""
file: test_api.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/bachya/pyden
"""

# -*- coding: utf-8 -*-
# pylint: disable=no-self-use,too-few-public-methods,redefined-outer-name
# pylint: disable=wildcard-import,unused-wildcard-import

import json

import requests_mock

import pyden
from tests.fixtures.trash import *

# pylint: disable=too-many-arguments


def test_bad_request(geocode_response_200, geocode_url,
                     place_lookup_response_200, place_lookup_url,
                     schedule_response_200, schedule_url):
    """ Tests a bad overall request """
    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_200))
        mock.get(place_lookup_url, text=json.dumps(place_lookup_response_200))
        mock.get(schedule_url, text=schedule_response_200)
        mock.get('https://recollect.net/api/bad_endpoint', status_code=404)

        with pytest.raises(pyden.exceptions.HTTPError) as exc_info:
            client = pyden.TrashClient('1234')
            client.get('bad_endpoint')
            assert '404 Client Error: Not Found' in str(exc_info)
