#!/usr/bin/python3
"""
Base Module.

Define the `Base` class that will be
the base of all other classes in this project.
"""


class Base:
    """
    This class will be the “base” of all other classes in this project.

    Attributes:
        __nb_objects (int): The number of created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        inistaniate the object.

        Args:
            id (int): Identfication number for instances
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
