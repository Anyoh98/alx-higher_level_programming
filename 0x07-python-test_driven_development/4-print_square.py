#!/usr/bin/python3
"""
This function will print a square using `# `
"""


def print_square(size):
    """
    Print a sqaure using `#`

    This function prints a square using the size inputed by the user

    Args:
        size (int): The size of the square

    Returns:
        None

    Raises:
        TypeError: If size is not an integer or is a float less than 0.
        ValueError: If size is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    square = [["#" for _ in range(size)] for _ in range(size)]
    for row in square:
        print("".join(row))
