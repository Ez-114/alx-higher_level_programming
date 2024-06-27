#!/usr/bin/python3
"""
The `is_same_class` Module defines a function called `is_same_class`.
This function is a customized function used to determine if the passed
Object is an instance of the passed class or not.
"""


def is_same_class(obj, a_class):
    """
    Determines if `obj` is exactly an instance of the specified class
    `a_class`.

    Args:
        obj (object): passed object to examine.
        a_class (class): passed class.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """

    return type(obj) is a_class
