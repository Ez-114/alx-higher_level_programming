#!/usr/bin/python3

"""
This module defines a Square class.

The Square class represents a square with a private attribute instance
attribute `size`. The size of a square is crucial for a square,
many things depend of it (area computation, etc...).
By keeping the size attribute private, the class can ensure control over
its type and value, thus maintaining the integrety of data.

The size attribute must be a non-negative integer.
"""


class Square:
    """
    A class used to represent a square.

    Attributes:
        __size (int): The size of the square, must be >= 0.
    """

    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
