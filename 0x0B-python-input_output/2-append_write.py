#!/usr/bin/python3
"""2-append_write
This module defines the `append_write` function that writes to a file
without deleting its old content.
"""


def append_write(filename="", text=""):
    """
    Appends text to a file.

    Args:
        filename (str, optional): the file name along with its path.
                Defaults to an empty string.
        text (str, optional): the text to insert. Defaults to an empty string.
    Returns:
        (int): total number of written bytes.
    """
    total_written = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        total_written = f.write(text)
    return total_written
