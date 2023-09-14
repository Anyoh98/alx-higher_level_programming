#!/usr/bin/python3
"""Defines an object attribute for the lookup function"""


def lookup(obj):
    """
    Return list of available attributes

    Args:
        obj (type): the object to inspect.

    Returns:
        list: A list of attribute names of the object.
    """

    return (dir(obj))
