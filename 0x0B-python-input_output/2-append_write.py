#!/usr/bin/python3
"""Module to append a string to the end of a text file and
return the number of characters added."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file and
    return the number of characters added.

    Args:
        filename (str): The name of the file to be appended
        (default is an empty string).
        text (str): The string to be appended to the file
        (default is an empty string).

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        characters_added = file.write(text)
        return characters_added
