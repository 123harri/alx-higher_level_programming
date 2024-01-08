#!/usr/bin/python3
"""Defines a rebel MyInt class."""


class MyInt(int):
    """A rebel class inheriting from int with inverted equality operators."""

    def __eq__(self, other):
        """Override the equality operator (==)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=)."""
        return super().__eq__(other)
