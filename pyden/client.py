"""
File: client.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/bachya
"""

import pyden.trash as trash


class Client(object):
    """ A client to interact with the city's web services """

    def __init__(self, coordinates, session=None):
        """ Initialize! """

        kwargs = {'session': session}

        self.trash = trash.Trash(coordinates, **kwargs)
