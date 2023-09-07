#!/usr/bin/python3
"""
This is the print name module.
It responsible for printing the first and last name of the user
"""


def say_my_name(first_name, last_name=""):
    """
    Print the users's first and last name.


    Arguments:
            first_name (str): The first name of the user
            last_name (str): The last name of the user


    Raises:
            TypeError: if first or lastname is not a string.


    Return:
            Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
