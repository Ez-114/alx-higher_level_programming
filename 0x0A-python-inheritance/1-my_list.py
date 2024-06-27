#!/usr/bin/python3
"""my_list Module

Defines the MyList class that inherit from the list base class.
"""


class MyList(list):
    """
    MyList class that inherit from the list base class.
    """

    def __init__(self):
        """Initialize the MyList instances."""
        super().__init__()

    def print_sorted(self):
        """Prints the list sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
