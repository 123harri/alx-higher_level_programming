#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Parameters:
    - matrix (list of lists): 2-dimensional array.

    Returns:
    - list of lists
    """
    result_matrix = matrix.copy()

    for i in range(len(matrix)):
        result_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (result_matrix)
