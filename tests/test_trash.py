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


def test_client_place_id(place_id):
    """ Tests the creation of a TrashClient from a place ID """
    client_manual = pyden.TrashClient(place_id)
    client_factory = pyden.TrashClient.from_place_id(place_id)
    assert client_manual.place_id == place_id
    assert client_manual == client_factory


def test_client_coordinates(coordinates, geocode_response_200, geocode_url,
                            place_id, place_lookup_response_200,
                            place_lookup_url):
    """ Tests the creation of a TrashClient from a latitude and longitude """
    latitude, longitude = coordinates

    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_200))
        mock.get(place_lookup_url, text=json.dumps(place_lookup_response_200))

        client_manual = pyden.TrashClient(place_id)
        client_factory = pyden.TrashClient.from_coordinates(
            latitude, longitude)
        assert client_factory.place_id == place_id
        assert client_manual.place_id == place_id


def test_schedule_successful(coordinates, geocode_response_200, geocode_url,
                             place_lookup_response_200, place_lookup_url,
                             schedule_response_200, schedule_url):
    """ Tests successfull retrieving the schedule """
    latitude, longitude = coordinates

    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_200))
        mock.get(place_lookup_url, text=json.dumps(place_lookup_response_200))
        mock.get(schedule_url, text=schedule_response_200)

        client = pyden.TrashClient.from_coordinates(latitude, longitude)
        assert client.schedule()


def test_schedule_unsuccessful(geocode_response_200):
    """ Tests an unsuccessful schedule lookup """
    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_200))
        mock.get(schedule_url, exc=Exception)

        with pytest.raises(Exception) as exc_info:
            client = pyden.TrashClient('12345')
            client.schedule()
            assert 'Unable to get trash schedule for place ID' in str(exc_info)


def test_unsuccessful_place_lookup(coordinates, geocode_response_200,
                                   geocode_url, place_lookup_response_404,
                                   place_lookup_url):
    """ Tests an unsuccessful place lookup """
    latitude, longitude = coordinates

    with requests_mock.Mocker() as mock:
        mock.get(geocode_url, text=json.dumps(geocode_response_200))
        mock.get(place_lookup_url, text=json.dumps(place_lookup_response_404))

        with pytest.raises(pyden.exceptions.GeocodingError) as exc_info:
            pyden.TrashClient.from_coordinates(latitude, longitude)
            assert 'Unable to get a valid schedule for address' in str(
                exc_info)
