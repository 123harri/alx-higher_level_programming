#!/usr/bin/python3
"""Defines a function for JSON serialization of a class instance."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
