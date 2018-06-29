"""Define tests for the client object."""
# pylint: disable=redefined-outer-name,unused-import
import json
from unittest.mock import PropertyMock
from urllib.parse import quote_plus

import aiohttp
import pytest

from pyden import Client

from .const import (
    TEST_CITY, TEST_COUNTRY, TEST_GOOGLE_API_KEY, TEST_LATITUDE,
    TEST_LONGITUDE, TEST_RECOLLECT_PLACE_ID, TEST_STATE, TEST_STREET_NAME,
    TEST_STREET_NUMBER, TEST_ZIP)


@pytest.fixture(scope='module')
def fixture_lookup():
    """Return an /api/lookup response."""
    return {
        "place": {
            "country": TEST_COUNTRY,
            "lat": TEST_LATITUDE,
            "locale": "en-US",
            "city": TEST_CITY,
            "name":
                '{0} {1}, {2}'.format(
                    TEST_STREET_NUMBER, TEST_STREET_NAME, TEST_CITY),
            "province": TEST_STATE,
            "unit": "",
            "lng": TEST_LONGITUDE,
            "street": TEST_STREET_NAME,
            "house": TEST_STREET_NUMBER,
            "id": TEST_RECOLLECT_PLACE_ID,
            "source": "recollect"
        }
    }


@pytest.mark.asyncio
async def test_init_coords(aresponses, event_loop, fixture_lookup, mocker):
    """Test initialization via coordinates."""
    mock_geocoder = mocker.patch('geocoder.google')

    type(mock_geocoder.return_value).city = PropertyMock(
        return_value=TEST_CITY)
    type(mock_geocoder.return_value).country_long = PropertyMock(
        return_value=TEST_COUNTRY)
    type(mock_geocoder.return_value).housenumber = PropertyMock(
        return_value=TEST_STREET_NUMBER)
    type(mock_geocoder.return_value).postal = PropertyMock(
        return_value=TEST_ZIP)
    type(mock_geocoder.return_value).state_long = PropertyMock(
        return_value=TEST_STATE)
    type(mock_geocoder.return_value).street_long = PropertyMock(
        return_value=TEST_STREET_NAME)

    aresponses.add(
        'recollect.net', '/api/lookup/{0},{1}.json'.format(
            TEST_LATITUDE, TEST_LONGITUDE), 'get',
        aresponses.Response(text=json.dumps(fixture_lookup), status=200))

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(websession)
        await client.trash.init_from_coords(
            TEST_LATITUDE, TEST_LONGITUDE, TEST_GOOGLE_API_KEY)
        assert client.trash.place_id == TEST_RECOLLECT_PLACE_ID
