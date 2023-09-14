#!/usr/bin/pthon3
"""Defines a class checking function"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exaclty an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match teh type of obj to.

    Returns:
        True if obj is exaclty an instance otherwise false
    """
    if type(obj) == a_class:
        return True
    return False
