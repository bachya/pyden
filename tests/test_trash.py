"""
file: test_trash.py
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


def test_bad_request(coordinates, geocode_response_200, geocode_url,
                     place_lookup_response_200, place_lookup_url,
                     schedule_response_200, schedule_url):
    """ Tests a bad overall request """

    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_200))
        mock.get(place_lookup_url, text=json.dumps(place_lookup_response_200))
        mock.get(schedule_url, text=schedule_response_200)
        mock.get('https://recollect.net/api/bad_endpoint', status_code=404)

        with pytest.raises(pyden.exceptions.HTTPError) as exc_info:
            client = pyden.Client(coordinates=coordinates)
            client.trash.get('bad_endpoint')
            assert '404 Client Error: Not Found' in str(exc_info)


def test_schedule_successful(coordinates, geocode_response_200, geocode_url,
                             place_lookup_response_200, place_lookup_url,
                             schedule_response_200, schedule_response_200_json,
                             schedule_url):
    """ Tests successfull retrieving the schedule """

    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_200))
        mock.get(place_lookup_url, text=json.dumps(place_lookup_response_200))
        mock.get(schedule_url, text=schedule_response_200)

        client = pyden.Client(coordinates=coordinates)
        assert client.trash.schedule() == schedule_response_200_json


def test_unsuccessful_geocode(coordinates, geocode_response_404, geocode_url):
    """ Tests an unsuccessful geocode lookup """

    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_404))

        with pytest.raises(pyden.exceptions.GeocodingError) as exc_info:
            pyden.Client(coordinates=coordinates)
            assert 'Unable to get an address for coordinates' in str(exc_info)


def test_unsuccessful_place_lookup(coordinates, geocode_response_200,
                                   geocode_url, place_lookup_response_404,
                                   place_lookup_url):
    """ Tests an unsuccessful place lookup """

    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_200))
        mock.get(place_lookup_url, text=json.dumps(place_lookup_response_404))

        with pytest.raises(pyden.exceptions.GeocodingError) as exc_info:
            pyden.Client(coordinates=coordinates)
            assert 'Unable to get a valid schedule for address' in str(
                exc_info)
