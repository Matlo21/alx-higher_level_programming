#!/usr/bin/python3
"""Module that defines a MyList class that inherits from list"""


class MyList(list):
    """a subclass of list"""

    def __init__(self):
        """initializes the object"""

        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""

        print(sorted(self))
