#!/usr/bin/python3
"""
The `inherits_from` Module defines a function called `inherits_from`.
This function is a customized function used to determine if the passed
Object is an instance of the passed class or not.
"""


def inherits_from(obj, a_class):
    """
    Determines if `obj` is an instance of a class that inherited
    (directly or indirectly) from the specified class `a_class`.

    Args:
        obj (object): passed object to examine.
        a_class (class): passed class.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """

    return type(obj) is not a_class and isinstance(obj, a_class)
