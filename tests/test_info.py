"""
File: test_info.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/bachya/pyden
"""

# -*- coding: utf-8 -*-

import pyden

def test_version():
    """ Test that we have a version """
    assert pyden.__author__ != ''
    assert pyden.__author_email__ != ''
    assert pyden.__copyright__ != ''
    assert pyden.__description__ != ''
    assert pyden.__license__ != ''
    assert pyden.__title__ != ''
    assert pyden.__url__ != ''
    assert pyden.__version__ != ''
