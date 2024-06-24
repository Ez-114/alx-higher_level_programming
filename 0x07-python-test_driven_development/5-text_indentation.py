#!/usr/bin/python3
"""Module Docstr"""


def text_indentation(text):
    """Function Docstr"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]

        if text[i] in ['.', '?', ':']:
            result += "\n\n"
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1

    print(result.strip(), end="")
