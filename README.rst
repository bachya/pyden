📡 pyden: A simple Python API for Tile® Bluetooth trackers
===========================================================

.. image:: https://travis-ci.org/bachya/pyden.svg?branch=master
  :target: https://travis-ci.org/bachya/pyden

.. image:: https://img.shields.io/pypi/v/pyden.svg
  :target: https://pypi.python.org/pypi/pyden

.. image:: https://img.shields.io/pypi/pyversions/pyden.svg
  :target: https://pypi.python.org/pypi/pyden

.. image:: https://img.shields.io/pypi/l/pyden.svg
  :target: https://github.com/bachya/pyden/blob/master/LICENSE

.. image:: https://codecov.io/gh/bachya/pyden/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/bachya/pyden

.. image:: https://api.codeclimate.com/v1/badges/6a3dbe1deaf343d90c01/maintainability
   :target: https://codeclimate.com/github/bachya/pyden/maintainability

.. image:: https://img.shields.io/badge/SayThanks-!-1EAEDB.svg
  :target: https://saythanks.io/to/bachya

pyden is a simple library to get data from the city and county of Denver, CO.

📡 PLEASE READ: 1.0.0 and Beyond
================================

Version 1.0.0 of pyden makes several breaking, but necessary changes:

* Moves the underlying library from
  `Requests <http://docs.python-requests.org/en/master/>`_ to
  `aiohttp <https://aiohttp.readthedocs.io/en/stable/>`_
* Changes the entire library to use :code:`asyncio`
* Makes 3.5 the minimum version of Python required

If you wish to continue using the previous, synchronous version of
pyden, make sure to pin version 1.1.2.

📡 Installation
===============

.. code-block:: bash

  $ pip install pyden

📡 Usage
========

.. code-block:: python

  import pyden

pyden starts within an
`aiohttp <https://aiohttp.readthedocs.io/en/stable/>`_ :code:`ClientSession`:

.. code-block:: python

  import asyncio

  from aiohttp import ClientSession

  from pyden import Client


  async def main() -> None:
      """Create the aiohttp session and run the example."""
      async with ClientSession() as websession:
          await run(websession)


  async def run(websession):
      """Run."""
      # YOUR CODE HERE

  asyncio.get_event_loop().run_until_complete(main())

Create a client:

.. code-block:: python

  client = pyden.Client(websession)

Then, get to it!

Trash Schedule
==============

.. code-block:: python

  # Initialize the trash module:
  await client.trash.init_from_coords(<lat>, <lon>, <google_api_key>)

  # Get the full schedule:
  await client.trash.schedule()

  # ...or get the date of next pickup:
  await client.trash.next_pickup(client.trash.PickupTypes.recycling)


📡 Contributing
===============

#. `Check for open features/bugs <https://github.com/bachya/pyden/issues>`_
   or `initiate a discussion on one <https://github.com/bachya/pyden/issues/new>`_.
#. `Fork the repository <https://github.com/bachya/pyden/fork>`_.
#. Install the dev environment: :code:`make init`.
#. Enter the virtual environment: :code:`pipenv shell`
#. Code your new feature or bug fix.
#. Write a test that covers your new functionality.
#. Run tests: :code:`make test`
#. Build new docs: :code:`make docs`
#. Add yourself to AUTHORS.rst.
#. Submit a pull request!
