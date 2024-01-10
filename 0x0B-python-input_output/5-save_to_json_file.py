#!/usr/bin/python3
"""Module to save an object to a text file using JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save the object to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
