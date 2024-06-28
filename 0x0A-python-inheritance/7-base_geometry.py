#!/usr/bin/python3
"""
This module defines a BaseGeometry class.

The BaseGeometry class is used to represent gometric concepts.
I includes methods like:
- area: currently not implemented but will be, in future.
- integer_validator: validates if the current passed value is an int.
"""


class BaseGeometry:
    """
    A class used to represent a BaseGeometry.
    """

    def area(self):
        """
        Raises an Exception to indicate that the area method
        is not implemented.

        Raises:
            Exception: Always raises an exception with
                the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the given value is an integer.

        Raises:
            TypeError: If value is not an integer.
             ValueError: If value is less than or equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
