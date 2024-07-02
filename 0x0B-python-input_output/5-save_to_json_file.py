#!/usr/bin/python3
"""5-save_to_json_file Module"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves data to a JSON file

    Args:
        my_obj (object): passed data object
        filename (str): name of the file
    """
    Json_data = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(Json_data)
