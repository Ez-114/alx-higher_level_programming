#!/usr/bin/python3
"""6-load_from_json_file.py Module"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a JSON file

    Args:
        filename (str): name of the file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
