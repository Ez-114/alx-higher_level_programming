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
        """Initialize the Square size with a given number or zero(Default)

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is not positive.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, new_size):
        """Sets the size of the square

        Args:
            new_size (int): The size of the square.

        Raises:
            TypeError: if new_size is not an integer
            ValueError: if new_size is not positive
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints to stdout the square represented by '#' character."""
        if (self.__size == 0):
            print()
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print('#', end='')
                print()
