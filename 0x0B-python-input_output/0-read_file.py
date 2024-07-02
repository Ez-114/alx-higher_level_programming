#!/usr/bin/python3
"""0-read_file Module
This module defines the `read_file` function that takes a file name
and prints its content after reading it.
"""


def read_file(file_name=""):
    """
    Opens a file and print its content to stdout after reading it.

    Args:
        file_name (str): a string object contains the file name with
            relative path.
    """

    with open(file_name, mode="r", encoding="utf-8") as a_file:
        print(a_file.read())
