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
        self.__width = width
        self.__height = height
