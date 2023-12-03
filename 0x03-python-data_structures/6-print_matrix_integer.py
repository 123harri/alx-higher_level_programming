#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers using str.format().
    """
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
