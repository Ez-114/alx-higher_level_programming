#!/usr/bin/python3

"""
This module defines a Square class.

The Square class represents a square with a private attribute instance
attribute `size`. The size of a square is crucial for a square,
many things depend of it (area computation, etc...).
By keeping the size attribute private, the class can ensure control over
its type and value, thus maintaining the integrety of data.
"""


class Square:
    """
    A class used to represent a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        initializes the Square with a given size.

        Attributes:
            size (int): The size of the square.
        """
        self.__size = size
