#!/usr/bin/python3
"""Defines a MyList class that inherits from list"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Function that prints the list but sorted
        """

        print(sorted(self))
