#!/usr/bin/python3
"""9-student.py"""


class Student:
    """Student calss"""

    def __init__(self, first_name, last_name, age):
        """init method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json method"""
        return self.__dict__
