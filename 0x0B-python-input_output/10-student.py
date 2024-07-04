#!/usr/bin/python3
"""10-student.py"""


class Student:
    """Student calss"""

    def __init__(self, first_name, last_name, age):
        """init method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json method"""
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list) \
                and all(isinstance(attr, str) for attr in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}

        return self.__dict__
