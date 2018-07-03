"""Define tests for the client object."""
# pylint: disable=redefined-outer-name,unused-import
import aiohttp
import pytest

from pyden import Client
from pyden.errors import RequestError


@pytest.mark.asyncio
async def test_request_error(aresponses, event_loop):
    """Test authenticating the device."""
    aresponses.add(
        'www.pollen.com', '/api/bad', 'get',
        aresponses.Response(text='', status=404))

    with pytest.raises(RequestError):
        async with aiohttp.ClientSession(loop=event_loop) as websession:
            client = Client(websession)
            await client.request('get', 'http://www.pollen.com/api/bad')
