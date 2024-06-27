#!/usr/bin/python3
"""lookup Module

Defines the `lookup` function.

It should take an object and return a list object containing all the
available attributes and methods.
"""


def lookup(obj):
    """
    This function inspects the given object and returns a list containing the
    names of its attributes and methods.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings representing the attributes and methods
                of the object.
    """
    return dir(obj)
