#!/usr/bin/python3
"""
Base Module.

Define the `Base` class that will be
the base of all other classes in this project.
"""
import json
import os


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

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            dictionary (dict): Key-value pairs of attributes to set.

        Returns:
            Base: An instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # type: ignore
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)  # type: ignore
        return dummy

    @classmethod
    def load_form_file(cls):
        """
        Returns a list of instances.

        The filename must be: <Class name>.json
            - example: Rectangle.json
        If the file doesn't exist, return an empty list.
        Otherwise, return a list of instances

        - the type of these instances depends on cls.

        Returns:
            list: List of instances.
        """

        file_name = "{}.json".format(cls.__name__)

        # search for the file
        if not os.path.exists(file_name):
            return []

        with open(file_name, mode="r", encoding="utf-8") as f:
            json_str = f.read()

        list_dicts = cls.from_json_string(json_str)
        instance_list = []
        for diction in list_dicts:
            instance_list.append(cls.create(**diction))
        return instance_list

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

    @staticmethod
    def from_json_string(json_string):
        """
        Static method. Recreates a list from the JSON string.

        Returns:
            list: containing dictionary objects that represent class instances.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
