#!/usr/bin/python3
"""say_my_name Module

The `say_my_name` module contains a single function, `say_my_name`,
which prints a formatted string containing
the provided first name and last name.
It ensures that the inputs are of the correct type and handles missing
last name by setting a default value.

The two inputs must be strings.
"""


def say_my_name(first_name, last_name=""):
    """say_my_name Function

    Prints a formatted string to `stdout` containing the provided
    first and last names.

    Output format:
        My name is <first name> <last name>

    Args:
        first_name (string): first name of the caller.
        last_name (string): last name of the caller.

    Raises:
        TypeError: If `first_name` is not a string.
        TypeError: If `last_name` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/3-say_my_name.txt')
