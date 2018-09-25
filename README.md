# 📡 pyden: A simple Python API for Denver, CO Data

[![Travis CI](https://travis-ci.org/bachya/pyden.svg?branch=master)](https://travis-ci.org/bachya/pyden)
[![PyPi](https://img.shields.io/pypi/v/pyden.svg)](https://pypi.python.org/pypi/pyden)
[![Version](https://img.shields.io/pypi/pyversions/pyden.svg)](https://pypi.python.org/pypi/pyden)
[![License](https://img.shields.io/pypi/l/pyden.svg)](https://github.com/bachya/pyden/blob/master/LICENSE)
[![Code Coverage](https://codecov.io/gh/bachya/pyden/branch/master/graph/badge.svg)](https://codecov.io/gh/bachya/pyden)
[![Maintainability](https://api.codeclimate.com/v1/badges/6a3dbe1deaf343d90c01/maintainability)](https://codeclimate.com/github/bachya/pyden/maintainability)
[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)

`pyden` is a simple library to get data from the city and county of Denver, CO.

# PLEASE READ: Version 1.0.0 and Beyond

Version 1.0.0 of `pyden` makes several breaking, but necessary changes:

* Moves the underlying library from
  [Requests](http://docs.python-requests.org/en/master/) to
  [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
* Changes the entire library to use `asyncio`
* Makes 3.6 the minimum version of Python required

If you wish to continue using the previous, synchronous version of
`pyden`, make sure to pin version 0.4.1.

# Installation

```python
 pip install pyden
```

# Usage

`pyden` starts within an
[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:

```python
import asyncio

from aiohttp import ClientSession

from pyden import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
      # YOUR CODE HERE


asyncio.get_event_loop().run_until_complete(main())
```

To create a client, simply:

```python
import asyncio

from aiohttp import ClientSession

from pyden import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
      client = Client(websession)


asyncio.get_event_loop().run_until_complete(main())
```

## Trash Schedule

```python
import asyncio

from aiohttp import ClientSession

from pyden import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
      client = Client(websession)

      # Initialize the trash module:
      await client.trash.init_from_coords(<LAT>, <LON>, "<GOOGLE_API_KEY>")

      # Get the full schedule:
      await client.trash.schedule()

      # ...or get the date of next pickup:
      await client.trash.next_pickup(client.trash.PickupTypes.recycling)


asyncio.get_event_loop().run_until_complete(main())
```

# Contributing

1. [Check for open features/bugs](https://github.com/bachya/pyden/issues)
  or [initiate a discussion on one](https://github.com/bachya/pyden/issues/new).
2. [Fork the repository](https://github.com/bachya/pyden/fork).
3. Install the dev environment: `make init`.
4. Enter the virtual environment: `pipenv shell`
5. Code your new feature or bug fix.
6. Write a test that covers your new functionality.
7. Run tests and ensure 100% code coverage: `make coverage`
8. Add yourself to `AUTHORS.md`.
9. Submit a pull request!
