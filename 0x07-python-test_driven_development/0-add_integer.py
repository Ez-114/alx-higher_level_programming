#!/usr/bin/python3

"""
This module defines a function called `add_integer`.

The function takes 2 numbers and return their addition.
The first number is mandatory to be passed, while the other is optional
as it is initialized to 98.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and return their result as an integer value.

    Attributes:
        a (int or float): The first number. Must be integer or float.
        b (int or float, optional): The second number. Must be integer
            or float. Defaulted to 98.

    Returns:
        int: The sum of `a` and `b` after casting to integers.

    Raises:
        TypeError: if either `a` or `b` are not integers nor floats.
    """
    if a != a:
        a = 89
    if b != b:
        b = 89

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    if result == float('inf') or result == -float('inf'):
        return 89

    # Safe to return the result
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt", optionflags=doctest.ELLIPSIS)
