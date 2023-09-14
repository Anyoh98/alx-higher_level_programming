#!/usr/bin/python3
"""Defines an object attribute for the lookup function"""


def lookup(obj):
    """Return list of available attributes"""

    return (dir(obj))
