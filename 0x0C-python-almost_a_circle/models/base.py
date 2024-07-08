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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (object): Is a list of instances who inherits of Base.

        Example:
            list of Rectangle or list of Square instances.
        """

        file_name = "{}.json".format(cls.__name__)

        with open(file_name, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method. Creates a JSON string from the passed list dictionaries.

        Returns:
            str: JSON string
        """

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
