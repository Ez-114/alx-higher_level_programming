#!/usr/bin/python3
"""print_square Module

This Module define the `print_square` function that takes `size` as argument
and prints to `stdout` a square with the given size.

`size` must be an integer value."""


def print_square(size):
    """print_square Function

    This function takes one argument (size) and prints a square of size
    `size` to `stdout`.

    Args:
        size (int): size of the square to be printed.

    Raises:
        TypeError: If size is not an integer.
        TypeError: If size is float and less than 0.
        ValueError: If size is an integer and less than 0.
    """
    if not isinstance(size, int) or isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print('#', end='')
        print()
