#!/usr/bin/python3
"""Defines the MyInt class that inherits from int class"""


class MyInt(int):
    """MyInt class definition"""
    def __eq__(self, obj):
        """Doc str"""
        return super().__ne__(obj)

    def __ne__(self, obj):
        """ doc str """
        return super().__eq__(obj)
