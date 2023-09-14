#!/usr/bin/python3
""" defines a class checking inherited function """


class BaseGeometry:
    """
    This is the BaseGeometry class.

    Methods:
        area(self): Raises an Exception with
        the message "area() is not implemented."

    Attributes:
        None
    """

    def area(self):
        """
        Public instance method that raises an
        Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")
