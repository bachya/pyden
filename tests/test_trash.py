"""Define tests for the client object."""
# pylint: disable=redefined-outer-name,unused-import
import json
from unittest.mock import PropertyMock

import aiohttp
import pytest

from pyden import Client
from pyden.errors import PydenError

from .const import (
    TEST_CITY,
    TEST_COUNTRY,
    TEST_GOOGLE_API_KEY,
    TEST_LATITUDE,
    TEST_LONGITUDE,
    TEST_RECOLLECT_PLACE_ID,
    TEST_STATE,
    TEST_STREET_NAME,
    TEST_STREET_NUMBER,
    TEST_ZIP,
)


@pytest.fixture(scope="module")
def fixture_lookup():
    """Return an /api/lookup response."""
    return {
        "place": {
            "country": TEST_COUNTRY,
            "lat": TEST_LATITUDE,
            "locale": "en-US",
            "city": TEST_CITY,
            "name": "{0} {1}, {2}".format(
                TEST_STREET_NUMBER, TEST_STREET_NAME, TEST_CITY
            ),
            "province": TEST_STATE,
            "unit": "",
            "lng": TEST_LONGITUDE,
            "street": TEST_STREET_NAME,
            "house": TEST_STREET_NUMBER,
            "id": TEST_RECOLLECT_PLACE_ID,
            "source": "recollect",
        }
    }


@pytest.fixture(scope="module")
def fixture_lookup_no_place():
    """Return an /api/lookup response without a place ID."""
    return {
        "place": {
            "country": TEST_COUNTRY,
            "lat": TEST_LATITUDE,
            "locale": "en-US",
            "city": TEST_CITY,
            "name": "{0} {1}, {2}".format(
                TEST_STREET_NUMBER, TEST_STREET_NAME, TEST_CITY
            ),
            "province": TEST_STATE,
            "unit": "",
            "lng": TEST_LONGITUDE,
            "street": TEST_STREET_NAME,
            "house": TEST_STREET_NUMBER,
            "source": "recollect",
        }
    }


@pytest.fixture(scope="module")
def fixture_schedule():
    """Return an .ics of the calendar schedule."""
    return r"""BEGIN:VCALENDAR
VERSION:2.0
METHOD:PUBLISH
PRODID:Data::ICal 0.22
X-PUBLISHED-TTL:1440
X-WR-CALDESC:Solid Waste
X-WR-CALNAME:8673 E 55th Ave\, Denver
X-WR-TIMEZONE:America/Denver
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20950529
SUMMARY:Trash and compost (sign-up only)
UID:2095-05-29-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycle\, and compost (sign-up only) - Pa
 int Drop-Off Event for Households and Businesses on Saturday\, June 23\, 2
 018 from 8 AM to 3 PM a t Dick’s Sporting Goods Park. For event details an
 d to select your expected arrival time\, visit https://www.paintcare.org/c
 ommercecity/. This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20950604
SUMMARY:Trash\, extra trash\, recycle\, and compost (sign-up only)
UID:2095-06-04-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20950611
SUMMARY:Trash and compost (sign-up only)
UID:2095-06-11-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycle\, and compost (sign-up only) - Paint Drop-Off E
 vent for Households and Businesses on Saturday\, June 23\, 2095 from 8 AM
 to 3 PM a t Dick’s Sporting Goods Park. For event details and to select yo
 ur expected arrival time\, visit https://www.paintcare.org/commercecity/.
 This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20950618
SUMMARY:Trash\, recycle\, and compost (sign-up only)
UID:2095-06-18-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20950625
SUMMARY:Trash and compost (sign-up only)
UID:2095-06-25-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycle\, and compost (sign-up only) - Pa
 int Drop-Off Event for Households and Businesses on Saturday\, June 23\, 2
 018 from 8 AM to 3 PM a t Dick’s Sporting Goods Park. For event details an
 d to select your expected arrival time\, visit https://www.paintcare.org/c
 ommercecity/. This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20950702
SUMMARY:Trash\, extra trash\, recycle\, and compost (sign-up only)
UID:2095-07-02-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20950709
SUMMARY:Trash and compost (sign-up only)
UID:2095-07-09-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycle\, and compost (sign-up only) - Paint Drop-Off E
 vent for Households and Businesses on Saturday\, June 23\, 2095 from 8 AM
 to 3 PM a t Dick’s Sporting Goods Park. For event details and to select yo
 ur expected arrival time\, visit https://www.paintcare.org/commercecity/.
 This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20950716
SUMMARY:Trash\, recycle\, and compost (sign-up only)
UID:2095-07-16-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20950723
SUMMARY:Trash and compost (sign-up only)
UID:2095-07-23-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycle\, and compost (sign-up only) - Pa
 int Drop-Off Event for Households and Businesses on Saturday\, June 23\, 2
 018 from 8 AM to 3 PM a t Dick’s Sporting Goods Park. For event details an
 d to select your expected arrival time\, visit https://www.paintcare.org/c
 ommercecity/. This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20950730
SUMMARY:Trash\, extra trash\, recycle\, and compost (sign-up only)
UID:2095-07-30-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20950806
SUMMARY:Trash and compost (sign-up only)
UID:2095-08-06-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycle\, and compost (sign-up only) - Paint Drop-Off E
 vent for Households and Businesses on Saturday\, June 23\, 2095 from 8 AM
 to 3 PM a t Dick’s Sporting Goods Park. For event details and to select yo
 ur expected arrival time\, visit https://www.paintcare.org/commercecity/.
 This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20950813
SUMMARY:Trash\, recycle\, and compost (sign-up only)
UID:2095-08-13-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20950820
SUMMARY:Trash and compost (sign-up only)
UID:2095-08-20-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycle\, and compost (sign-up only) - Pa
 int Drop-Off Event for Households and Businesses on Saturday\, June 23\, 2
 018 from 8 AM to 3 PM a t Dick’s Sporting Goods Park. For event details an
 d to select your expected arrival time\, visit https://www.paintcare.org/c
 ommercecity/. This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20950827
SUMMARY:Trash\, extra trash\, recycle\, and compost (sign-up only)
UID:2095-08-27-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20950904
SUMMARY:Trash and compost (sign-up only)
UID:2095-09-04-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycle\, and compost (sign-up only) - Paint Drop-Off E
 vent for Households and Businesses on Saturday\, June 23\, 2095 from 8 AM
 to 3 PM a t Dick’s Sporting Goods Park. For event details and to select yo
 ur expected arrival time\, visit https://www.paintcare.org/commercecity/.
 This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20950910
SUMMARY:Trash\, recycle\, and compost (sign-up only)
UID:2095-09-10-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20950917
SUMMARY:Trash and compost (sign-up only)
UID:2095-09-17-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycle\, and compost (sign-up only) - Pa
 int Drop-Off Event for Households and Businesses on Saturday\, June 23\, 2
 018 from 8 AM to 3 PM a t Dick’s Sporting Goods Park. For event details an
 d to select your expected arrival time\, visit https://www.paintcare.org/c
 ommercecity/. This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20950924
SUMMARY:Trash\, extra trash\, recycle\, and compost (sign-up only)
UID:2095-09-24-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20951001
SUMMARY:Trash and compost (sign-up only)
UID:2095-10-01-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycle\, and compost (sign-up only) - Paint Drop-Off E
 vent for Households and Businesses on Saturday\, June 23\, 2095 from 8 AM
 to 3 PM a t Dick’s Sporting Goods Park. For event details and to select yo
 ur expected arrival time\, visit https://www.paintcare.org/commercecity/.
 This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20951008
SUMMARY:Trash\, recycle\, and compost (sign-up only)
UID:2095-10-08-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20951015
SUMMARY:Trash and compost (sign-up only)
UID:2095-10-15-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycle\, and compost (sign-up only) - Pa
 int Drop-Off Event for Households and Businesses on Saturday\, June 23\, 2
 018 from 8 AM to 3 PM a t Dick’s Sporting Goods Park. For event details an
 d to select your expected arrival time\, visit https://www.paintcare.org/c
 ommercecity/. This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20951022
SUMMARY:Trash\, extra trash\, recycle\, and compost (sign-up only)
UID:2095-10-22-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20951029
SUMMARY:Trash and compost (sign-up only)
UID:2095-10-29-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycle\, and compost (sign-up only) - Paint Drop-Off E
 vent for Households and Businesses on Saturday\, June 23\, 2095 from 8 AM
 to 3 PM a t Dick’s Sporting Goods Park. For event details and to select yo
 ur expected arrival time\, visit https://www.paintcare.org/commercecity/.
 This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20951105
SUMMARY:Trash\, recycle\, and compost (sign-up only)
UID:2095-11-05-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20951112
SUMMARY:Trash and compost (sign-up only)
UID:2095-11-12-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycle\, and compost (sign-up only) - Pa
 int Drop-Off Event for Households and Businesses on Saturday\, June 23\, 2
 018 from 8 AM to 3 PM a t Dick’s Sporting Goods Park. For event details an
 d to select your expected arrival time\, visit https://www.paintcare.org/c
 ommercecity/. This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20951119
SUMMARY:Trash\, extra trash\, recycle\, and compost (sign-up only)
UID:2095-11-19-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20951126
SUMMARY:Trash and compost (sign-up only)
UID:2095-11-26-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycle\, and compost (sign-up only) - Paint Drop-Off E
 vent for Households and Businesses on Saturday\, June 23\, 2095 from 8 AM
 to 3 PM a t Dick’s Sporting Goods Park. For event details and to select yo
 ur expected arrival time\, visit https://www.paintcare.org/commercecity/.
 This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20951203
SUMMARY:Trash\, recycle\, and compost (sign-up only)
UID:2095-12-03-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20951210
SUMMARY:Trash and compost (sign-up only)
UID:2095-12-10-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycle\, and compost (sign-up only) - Pa
 int Drop-Off Event for Households and Businesses on Saturday\, June 23\, 2
 018 from 8 AM to 3 PM a t Dick’s Sporting Goods Park. For event details an
 d to select your expected arrival time\, visit https://www.paintcare.org/c
 ommercecity/. This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20951217
SUMMARY:Trash\, extra trash\, recycle\, and compost (sign-up only)
UID:2095-12-17-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only) - Paint Drop-Off Event for Hou
 seholds and Businesses on Saturday\, June 23\, 2095 from 8 AM to 3 PM a t
 Dick’s Sporting Goods Park. For event details and to select your expected
 arrival time\, visit https://www.paintcare.org/commercecity/. This event i
 s open to all Colorado residents.
DTSTART;VALUE=DATE:20951224
SUMMARY:Trash and compost (sign-up only)
UID:2095-12-24-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycle\, and compost (sign-up only) - Paint Drop-Off E
 vent for Households and Businesses on Saturday\, June 23\, 2095 from 8 AM
 to 3 PM a t Dick’s Sporting Goods Park. For event details and to select yo
 ur expected arrival time\, visit https://www.paintcare.org/commercecity/.
 This event is open to all Colorado residents.
DTSTART;VALUE=DATE:20951231
SUMMARY:Trash\, recycle\, and compost (sign-up only)
UID:2095-12-31-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Recycle - Paint Drop-Off Event for Households and Businesses on
  Saturday\, June 23\, 2095 from 8 AM to 3 PM a t Dick’s Sporting Goods Par
 k. For event details and to select your expected arrival time\, visit http
 s://www.paintcare.org/commercecity/. This event is open to all Colorado re
 sidents.
DTSTART;VALUE=DATE:20190114
SUMMARY:Recycle
UID:2019-01-14-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Recycle - Paint Drop-Off Event for Households and Businesses on
  Saturday\, June 23\, 2095 from 8 AM to 3 PM a t Dick’s Sporting Goods Par
 k. For event details and to select your expected arrival time\, visit http
 s://www.paintcare.org/commercecity/. This event is open to all Colorado re
 sidents.
DTSTART;VALUE=DATE:20190128
SUMMARY:Recycle
UID:2019-01-28-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Recycle - Paint Drop-Off Event for Households and Businesses on
  Saturday\, June 23\, 2095 from 8 AM to 3 PM a t Dick’s Sporting Goods Par
 k. For event details and to select your expected arrival time\, visit http
 s://www.paintcare.org/commercecity/. This event is open to all Colorado re
 sidents.
DTSTART;VALUE=DATE:20190211
SUMMARY:Recycle
UID:2019-02-11-Denver-waste-@recollect.net
END:VEVENT
END:VCALENDAR"""


def setup_mock_geocoder(mocker) -> None:
    """Create a mock geocoder object."""
    mock_geocoder = mocker.patch("pyden.trash.google")
    type(mock_geocoder.return_value).city = PropertyMock(return_value=TEST_CITY)
    type(mock_geocoder.return_value).country_long = PropertyMock(
        return_value=TEST_COUNTRY
    )
    type(mock_geocoder.return_value).housenumber = PropertyMock(
        return_value=TEST_STREET_NUMBER
    )
    type(mock_geocoder.return_value).postal = PropertyMock(return_value=TEST_ZIP)
    type(mock_geocoder.return_value).state_long = PropertyMock(return_value=TEST_STATE)
    type(mock_geocoder.return_value).street_long = PropertyMock(
        return_value=TEST_STREET_NAME
    )


@pytest.mark.asyncio
async def test_init_coords(aresponses, event_loop, fixture_lookup, mocker):
    """Test initialization via coordinates."""
    setup_mock_geocoder(mocker)

    aresponses.add(
        "recollect.net",
        "/api/lookup/{0},{1}.json".format(TEST_LATITUDE, TEST_LONGITUDE),
        "get",
        aresponses.Response(text=json.dumps(fixture_lookup), status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(websession)
        await client.trash.init_from_coords(
            TEST_LATITUDE, TEST_LONGITUDE, TEST_GOOGLE_API_KEY
        )
        assert client.trash.place_id == TEST_RECOLLECT_PLACE_ID


@pytest.mark.asyncio
async def test_next_pickup(
    aresponses, event_loop, fixture_lookup, fixture_schedule, mocker
):
    """Test calling a method before there's a place ID."""
    setup_mock_geocoder(mocker)

    aresponses.add(
        "recollect.net",
        "/api/lookup/{0},{1}.json".format(TEST_LATITUDE, TEST_LONGITUDE),
        "get",
        aresponses.Response(text=json.dumps(fixture_lookup), status=200),
    )
    aresponses.add(
        "recollect.a.ssl.fastly.net",
        "/api/places/{0}/services/248/events.en-US.ics".format(TEST_RECOLLECT_PLACE_ID),
        "get",
        aresponses.Response(text=fixture_schedule, status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(websession)
        await client.trash.init_from_coords(
            TEST_LATITUDE, TEST_LONGITUDE, TEST_GOOGLE_API_KEY
        )
        next_recycling_date = await client.trash.next_pickup(
            client.trash.PickupTypes.recycling
        )
        assert str(next_recycling_date) == "2095-06-04 00:00:00-07:00"


@pytest.mark.asyncio
async def test_no_place_found(aresponses, event_loop, fixture_lookup_no_place, mocker):
    """Test no valid place ID coming from init."""
    setup_mock_geocoder(mocker)

    aresponses.add(
        "recollect.net",
        "/api/lookup/{0},{1}.json".format(TEST_LATITUDE, TEST_LONGITUDE),
        "get",
        aresponses.Response(text=json.dumps(fixture_lookup_no_place), status=200),
    )

    with pytest.raises(PydenError):
        async with aiohttp.ClientSession(loop=event_loop) as websession:
            client = Client(websession)
            await client.trash.init_from_coords(
                TEST_LATITUDE, TEST_LONGITUDE, TEST_GOOGLE_API_KEY
            )


@pytest.mark.asyncio
async def test_schedule(
    aresponses, event_loop, fixture_lookup, fixture_schedule, mocker
):
    """Test calling a method before there's a place ID."""
    setup_mock_geocoder(mocker)

    aresponses.add(
        "recollect.net",
        "/api/lookup/{0},{1}.json".format(TEST_LATITUDE, TEST_LONGITUDE),
        "get",
        aresponses.Response(text=json.dumps(fixture_lookup), status=200),
    )
    aresponses.add(
        "recollect.a.ssl.fastly.net",
        "/api/places/{0}/services/248/events.en-US.ics".format(TEST_RECOLLECT_PLACE_ID),
        "get",
        aresponses.Response(text=fixture_schedule, status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(websession)
        await client.trash.init_from_coords(
            TEST_LATITUDE, TEST_LONGITUDE, TEST_GOOGLE_API_KEY
        )
        schedule = await client.trash.upcoming_schedule()
        assert len(schedule) == 32


@pytest.mark.asyncio
async def test_schedule_no_place(aresponses, event_loop, fixture_lookup, mocker):
    """Test calling a method before there's a place ID."""
    setup_mock_geocoder(mocker)

    aresponses.add(
        "recollect.net",
        "/api/lookup/{0},{1}.json".format(TEST_LATITUDE, TEST_LONGITUDE),
        "get",
        aresponses.Response(text=json.dumps(fixture_lookup), status=200),
    )

    with pytest.raises(PydenError):
        async with aiohttp.ClientSession(loop=event_loop) as websession:
            client = Client(websession)
            await client.trash.upcoming_schedule()
