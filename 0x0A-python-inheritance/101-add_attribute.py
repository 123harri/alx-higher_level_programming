#!/usr/bin/python3
"""Defines a function to add a new attribute to an object."""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attr (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if "__dict__" in dir(obj):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
