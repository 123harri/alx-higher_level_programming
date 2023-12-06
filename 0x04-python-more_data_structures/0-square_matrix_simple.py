#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Parameters:
    - matrix (list of lists): 2-dimensional array.

    Returns:
    - list of lists: New matrix with each value being the square of the corresponding input value.
    """
    result_matrix = [[0] * len(row) for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
