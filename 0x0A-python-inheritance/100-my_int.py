#!/usr/bin/python3
"""defines a class mtint"""


class MyInt(int):
    """invert the int operators"""

    def __eq__(self, value):
        """overide == opertor"""
        return self.real != value

    def __ne__(self, value):
        """overide != operator"""
        return self.real == value
