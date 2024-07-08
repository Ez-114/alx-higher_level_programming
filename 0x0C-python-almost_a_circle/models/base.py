#!/usr/bin/python3
"""
Base Module.

Define the `Base` class that will be
the base of all other classes in this project.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method. Creates a JSON string from the passed list dictionaries.

        Returns:
            str: JSON string
        """

        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
