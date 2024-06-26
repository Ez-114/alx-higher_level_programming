#!/usr/bin/python3
"""0-rectangle Module

This Module contains the `Rectangel` class implementation
"""


class Rectangle:
    """Rectangel Class

    This class represents a Rectangle.

    Attributes:
            __width (int): the width of the Rectangle object.
            __height (int): the height of the Rectangle object.
            number_of_instances (int): public class attr that keeps
                    track of instances count. Initialized to 0.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle instance attributes.

        Args:
            width (int, optional): the width of the Rectangle object.
                        Defaulted to 0. Must be a non-negative integer.
            height (int, optional): the height of the Rectangle object.
                        Defaulted to 0. Must be a non-negative integer.

            Raises:
                TypeError: If width or height are not integers.
                ValueError: If width or height are < 0.
       """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns a string of the rectangle represented by '#' character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        result = (str(self.print_symbol) * self.__width) + '\n'
        result *= self.__height
        return result[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """
        Gets the width value of the Rectangle object

        Returns:
            int: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the square.

        Args:
            value (int): the width of the Rectangle object.

        Raises:
            TypeError: if value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Gets the height value of the Rectangle object

        Returns:
            int: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the square.

        Args:
            value (int): the height of the Rectangle object.

        Raises:
            TypeError: if value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates the area of the current Rectangle Instance.

        Returns:
            int: The calculated area.
        """
        result = self.__width * self.__height

        return result

    def perimeter(self):
        """
        Calculates the perimeter of the current Rectangle Instance.

        Returns:
            int: The calculated perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        result = self.__width + self.__height
        result *= 2

        return result

    def __del__(self):
        """
        Called after the class instance is deleted succefully.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
