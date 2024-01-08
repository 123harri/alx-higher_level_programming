#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Raise an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
