#!/usr/bin/python3
"""Module to write a string to a text file and
return the number of characters written."""


def write_file(filename="", text=""):
    """Write a string to a text file and
    return the number of characters written.

    Args:
        filename (str): The name of the file to be written
        (default is an empty string).
        text (str): The string to be written to the file
        (default is an empty string).

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        characters_written = file.write(text)
        return characters_written + text.count('\n')
