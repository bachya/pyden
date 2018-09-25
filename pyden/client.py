"""Define a client to interact with the city and county of Denver."""
from typing import Union

from aiohttp import ClientSession, client_exceptions

from .errors import RequestError
from .trash import Trash


class Client:  # pylint: disable=too-few-public-methods
    """Define the client."""

    def __init__(self, websession: ClientSession) -> None:
        """Initialize."""
        self._websession = websession

        self.trash = Trash(self.request, websession.loop)

    async def request(
            self,
            method: str,
            url: str,
            *,
            kind: str = 'json',
            headers: dict = None,
            params: dict = None,
            json: dict = None) -> Union[str, dict]:
        """Make a request."""
        async with self._websession.request(method, url, headers=headers,
                                            params=params, json=json) as resp:
            try:
                resp.raise_for_status()
                if kind == 'text':
                    data = await resp.text()
                else:
                    data = await resp.json(content_type=None)
                return data
            except client_exceptions.ClientError as err:
                raise RequestError(
                    'Error requesting data from {0}: {1}'.format(
                        url, err)) from None
