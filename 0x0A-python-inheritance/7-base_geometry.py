#!/usr/bin/python3
"""Defines a base geometry class Base geometry"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    Methods:
        area(self): Raises an Exception with the message "area()
        is not implemented."
        integer_validator(self, name, value): Validates an integer value.

    Attributes:
        None
    """

    def area(self):
        """
        Public instance method that raises an
        Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
