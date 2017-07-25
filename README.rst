pyden: data from the City and County of Denver, CO
==================================================

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

.. image:: https://img.shields.io/codeclimate/github/bachya/pyden.svg
  :target: https://codeclimate.com/github/bachya/pyden

.. image:: https://img.shields.io/badge/SayThanks-!-1EAEDB.svg
  :target: https://saythanks.io/to/bachya

.. Regenmaschine (German for "rain machine") is a simple, clean, well-tested Python
.. library for interacting with `RainMachine™ smart sprinkler controllers
.. <http://www.rainmachine.com/>`_. It gives developers an easy API to manage their
.. controllers over a LAN or via RainMachine™'s cloud.

.. 💧 Installation
.. ===============

.. .. code-block:: bash

..   $ pip install regenmaschine

.. 💧 Example
.. ==========

.. .. code-block:: python

..   import regenmaschine as rm

..   # Authenticate against the local device or the remote API:
..   auth = rm.Authenticator.create_local('192.168.1.100', 'MY_RM_PASSWORD')
..   auth = rm.Authenticator.create_remote('EMAIL_ADDRESS', 'MY_RM_PASSWORD')

..   # Create a client:
..   client = rm.Client(auth)

..   # Get information on all programs:
..   program_info = client.programs.all()

..   # Turn on program 1:
..   client.programs.start(1)

..   # Stop program 1:
..   client.programs.stop(1)

..   # Get information on all zones:
..   zone_info = client.zones.all()

..   # Turn on zone 3 for 5 minutes:
..   client.zones.start(3, 300)

.. 💧 More Information
.. ===================

.. Full documentation for Regenmaschine can be found here: http://bachya.github.io/regenmaschine

.. 💧 Contributing
.. ===============

.. #. `Check for open features/bugs <https://github.com/bachya/regenmaschine/issues>`_
..    or `initiate a discussion on one <https://github.com/bachya/regenmaschine/issues/new>`_.
.. #. `Fork the repository <https://github.com/bachya/regenmaschine/fork>`_.
.. #. Install the dev environment: :code:`make init`.
.. #. Enter the virtual environment: :code:`pipenv shell`
.. #. Code your new feature or bug fix.
.. #. Write a test that covers your new functionality.
.. #. Run tests: :code:`make test`
.. #. Build new docs: :code:`make docs`
.. #. Add yourself to AUTHORS.rst.
.. #. Submit a pull request!
