#!/usr/bin/python3
"""1-write_file Module
This module defines the `write_file` function that takes 2 arguments:
The file name and the text to insert into the file. It does not reserve
the old content in the file.
"""


def write_file(file_name="", text=""):
    """
    Writes text into a file. It deletes the file's old content if there exists.

    Args:
        file_name (str, optional): the name of the file with its relative path.
                Defaulted to an empty string.
        text (str, optional): the text to insert into the given file.
                Defaulted to an empty string.
    Returns:
        (int): The total bytes written to the given file.
    """
    total_written = 0
    with open(file_name, mode="w", encoding="utf-8") as a_file:
        total_written = a_file.write(text)

    return total_written
