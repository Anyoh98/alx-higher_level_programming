#!/usr/bin/python3
"""defines a rectangle subclass squre"""
Rectangle = __import__('9-rectangle').Rectangle


class square(Rectangle):
    """rep a square"""

    def __init__(self, size):
        """ini a new square.

        Args:
            size (int): The size of new sauere.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
