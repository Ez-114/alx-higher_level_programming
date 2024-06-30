#!/usr/bin/python3
"""doctstr"""


def add_attribute(obj, name, val):
    """docstr"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
