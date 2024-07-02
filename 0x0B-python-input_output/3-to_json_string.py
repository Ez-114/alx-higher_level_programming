#!/usr/bin/python3
"""3-to_json_string
This module defines the `to_json_string` function that retruns the JSON
representation of an object(string).
"""
import json


def to_json_string(my_obj):
    """
    Converts `my_obj` to its JSON string representation.

    Args:
        my_obj (object): passed object to be converted.
    Returns:
        (str): the string representation of the passed object.
    """
    return json.dumps(my_obj)
