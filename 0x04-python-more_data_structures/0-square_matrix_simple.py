#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Square_matriz_simple

    Computes the square of each value in a given matrix

    Args:
        matrix: n*m nested list
    Return:
        new_matrix -> a squared version of the passed one
    """

    if not matrix:
        return matrix

    # Create a new empty matrix to store the squared values
    new_mat = []

    # Loop throw each row in OG matrix and go in each column to square its val
    for row in matrix:
        # Create a sub-list for each newly squared row
        squared_row = [val ** 2 for val in row]

        # Add the new row to the result i.e. new_mat
        new_mat.append(squared_row)

    return new_mat
