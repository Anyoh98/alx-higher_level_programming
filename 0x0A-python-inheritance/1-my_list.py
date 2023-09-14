#!/usr/bin/python3
""" This script defines an inherited list class called MyList"""


class MyList(list):
    """ Class My list that inherits from another class 'list'."""

    def print_sorted(self):
        """
        function that prints a sorted list

        Args:
            self

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
