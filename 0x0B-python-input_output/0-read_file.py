#!/usr/bin/python3
"""Module to read and print the content of a text file."""


def read_file(filename=""):
    """Read and print the content of a text file.

    Args:
        filename (str): The name of the file to be read
        (default is an empty string).
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
