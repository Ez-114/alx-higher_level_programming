#!/usr/bin/python3
"""Defines Square class That inherits from Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle class

    Attributes:
        __size (int): size
    """

    def __init__(self, size):
        """initializes the Square Object instance

        Args:
            size: size of the square size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """area method"""
        return self.__size * self.__size
