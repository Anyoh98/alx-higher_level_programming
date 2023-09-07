#!/usr/bin/python3
"""
This function adds 2 intgers
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers or floats a and b and returns result.
    Formula: a + b
    Raises:
        TypeError: if 'a' or 'b' are not floats or integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
