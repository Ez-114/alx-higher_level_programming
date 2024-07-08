#!/usr/bin/python3
"""
Square Module.

This module defines the `Square` class,
which inherits from the `Base` class.

The `Square` class models a Square
with specific attributes and methods
to manipulate and display its properties.

Classes:
    Square: A class representing a Square,
    inheriting from the `Base` class.

Usage Example:
    from models.Square import Square

    # Creating a Square instance
    sq = Square(10, 10, 5, 5, 1)

    # Accessing attributes
    print(sq.width)  # Output: 10
    print(sq.height)  # Output: 20

    # Updating attributes
    sq.update(2, 30)
    sq.update(size=15)

    # Displaying the Square
    sq.display()
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Blueprint for Square objects.
    Inherits from the `Rectangle` class.

    Attributes:
        id (int): The Identfication number of the instance
        size (int): The size of the Square (equal to width and height).
        __x (int): Private instance attribute that holds the
                            X co-ordinated of the square instance
                            in the XY-plane. Defaults to 0.
        __y (int): Private instance attribute that holds the
                            Y co-ordinated of the square instance
                            in the XY-plane. Defaults to 0.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the square instance.

        Args:
            size (int): The size of the Square (equal to width and height).
            x (int, optional): Private instance attribute that holds the
                            X co-ordinated of the square instance
                            in the XY-plane. Defaults to 0.
            y (int, optional): Private instance attribute that holds the
                            Y co-ordinated of the square instance
                            in the XY-plane. Defaults to 0.
            id (int): The Identfication number of the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Creates a new string object from the given Square instance.

        Returns:
            (str): The created str object.
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )
