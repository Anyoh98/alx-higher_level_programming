#!/usr/bin/python3
""" defines a class rectangle that inherits from the basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ Initialize a ne rectangle.

        Args:
            width (int): The width of teh new rectangle.
            height (int): The height of teh new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
