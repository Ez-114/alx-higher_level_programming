#!/usr/bin/python3
"""4-from_json_string
This module defines the `from_json_string` function that
retruns the object (Python data structure) represented
by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Converts `my_str` to its original object.

    Args:
        my_str (str): a JSON string representation.
    Returns:
        (object): the original form of the JSON string.
    """
    return json.loads(my_str)
