#!/usr/bin/python3

"""
This module defines the ``matrix_divided`` function.

This function takes 2 inputs and return 1. The first input is a 2D matrix,
list of lists, and the second input is the number that will divide every
element in the matrix.

First imput must be a list of lists of integers or floats or both.
The second input must be an integer or a float.
"""


def matrix_divided(matrix, div):
    """
    Divides matrix elements by the number ``div``.

    Args:
        matrix (list): First input. Must be list of lists.
            Must contain integers or floats.
        div (int or float): Second input. Must be an integer or float.
            Must not be 0.

    Raises:
        TypeError: if matrix is not a list of lists or
            if rows in matrix have different lengths or
            div or matrix elements are not integers or floats.
        ZeroDivisionError: if div is Zero 0.
    """
    # first check for div
    if div is None or not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Now check for matrix and its elements
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    og_len = len(matrix[0])  # This contains the length of first row
    divided_matrix = []  # to store the divided mat
    for i, row in enumerate(matrix):
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if og_len != len(row):  # Compares each row with the first row's len
            raise TypeError("Each row of the matrix must have the same size")

        divided_row = []  # to store each divided row
        for j, col in enumerate(row):
            # handel elements types
            if not isinstance(col, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

            # do calculation
            new_val = col / div
            divided_row.append(round(new_val, 2))

        divided_matrix.append(divided_row)

    return divided_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/2-matrix_divided.txt')
