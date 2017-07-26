"""
file: test_util.py
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


def test_bad_request(coordinates, geocode_response_404, geocode_url):
    """ Tests a bad overall request """
    latitude, longitude = coordinates

    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_404))

        with pytest.raises(pyden.exceptions.GeocodingError) as exc_info:
            pyden.TrashClient.from_coordinates(
                latitude, longitude, cache=False)
            assert 'Unable to get an address for coordinates' in str(exc_info)
