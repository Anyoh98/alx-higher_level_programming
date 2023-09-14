#!/usr/bin/python3
""" Defines a class and inherited class checking fucntion """


def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an instance of a 
    specified class or a subclass.

    Args:
    obj (object): The object to check.
    a_class (class): The class to compare against.

    Returns:
    bool: True if the object is an instance of the specified class or 
    its subclass; False otherwise.
    """
    def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
