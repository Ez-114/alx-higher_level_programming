#!/usr/bin/python3
"""
Rectangle Module.

Defines the `Rectangle` class that inherits from the `Base` class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Blueprint for Rectangle objects.
    Inherits from the `Base` class.

    Attributes:
        id (int): The Identfication number of the instance
        __width (int): Private instance attribute holding the width
                        of the rectangle instance.
        __height (int): Private instance attribute holding the height
                        of the rectangle instance.
        __x (int): Private instance attribute that holds the
                            X co-ordinated of the rectangel instance
                            in the XY-plane. Defaults to 0.
        __y (int): Private instance attribute that holds the
                            Y co-ordinated of the rectangel instance
                            in the XY-plane. Defaults to 0.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initiates the Rectangle calss instance.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int, optional): The X co-ordinates on the XY-plane.
                                Defaults to 0.
            y (int, optional): The Y co-ordinates of the XY-plane.
                                Defaults to 0.
            id (int, optional): The Identfication number
                                of the initiated instance. Defaults to `None`.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the Rectangle instance.

        Returns:
            int: The width attribute.
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Sets the width attribute of the Rectangle instance.

        Args:
            val (int): The new width value.
        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        """
        Get the height of the Rectangle instance.

        Returns:
            int: The height attribute.
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Sets the height attribute of the Rectangle instance.

        Args:
            val (int): The new height value.
        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        """
        Get the x of the Rectangle instance.

        Returns:
            int: The x attribute.
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        Sets the x attribute of the Rectangle instance.

        Args:
            val (int): The new x value.
        """
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """
        Get the y of the Rectangle instance.

        Returns:
            int: The y attribute.
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        Sets the y attribute of the Rectangle instance.

        Args:
            val (int): The new y value.
        """
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return (self.width * self.height)

    def display(self):
        """
        Prints in `stdout` the Rectangle instance with the character #
        """
        if self.width == 0 or self.height == 0:
            print()
        else:
            print("\n" * self.y, end="")
            for _ in range(self.height):
                print(" " * self.x, end="")
                print("#" * self.width)

    def __str__(self):
        """
        Creates a new string object from the given Rectangle
        instance.

        Returns:
            (str): The created str object.
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                                                    self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height
                                                )
