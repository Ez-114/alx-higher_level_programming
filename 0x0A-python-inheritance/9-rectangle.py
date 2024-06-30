#!/usr/bin/python3
"""Defines the Rectangle class that inherit from BaseGeometry class"""
bg = __import__("7-base_geometry").BaseGeometry


class Rectangle(bg):
    """inherits from BaseGeometry class

    Attributes:
        __width (int): width
        __height (int): height
    """

    def __init__(self, width, height):
        """initializes the Rectangle Object instance

        Args:
            width: width of the Rectangle
            height: height of the Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """overrides the un-implemented area method in the
        BaseGeometry class.

        Returns:
            (int): area of the Rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """constructs the representation of a rectangle.

        Returns:
            str: string representation of the instansiated Rectangle class
        """

        rp = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return rp
