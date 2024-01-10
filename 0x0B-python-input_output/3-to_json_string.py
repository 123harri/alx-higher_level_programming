#!/usr/bin/python3
"""Module to convert an object to its JSON representation."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
