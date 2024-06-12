#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square with two private instance
attributes `size` and `position`. The size of a square is crucial for a square,
many things depend of it (area computation, etc...). The position tells where
does the square actually lies on the (x, y) plane.
By keeping both attributes private, the class can ensure control over
its types and values, thus maintaining the integrety of data.

The size attribute must be a non-negative integer.
The position attribute must be a tuple of 2 positive integers.
"""


class Square:
    """
    A class used to represent a square.

    Attributes:
        __size (int): The size of the square, must be >= 0.
        __position (tuple): the positoin of the square on (x, y) plane,
            Must be 2 non negative integers.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square size with a given number and Square position
        to a given tuple.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): the position of the square
                on (x, y) plane.
                Defaults to (0, 0).

        Raises:
            TypeError: if size is not an integer or position is not a tuple.
            ValueError: if size is not positive.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            tuple: the position of the square on the (x, y) plane.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): the position of the square on the (x, y) plane.

        Raises:
            TypeError: if value is not a tuple or if tuple elements
                are not integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(val, int) for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints to stdout the square represented by '#' character.
        If size is 0, prints an empty line.
        Position is used by adding space before printing the square.
        """
        if self.__size == 0:
            print()
            return

        for row in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
