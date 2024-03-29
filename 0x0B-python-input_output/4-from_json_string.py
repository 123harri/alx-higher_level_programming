#!/usr/bin/python3
"""Module to convert a JSON string to a Python data structure."""

import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
