#!/usr/bin/python3
"""Definition for a locked class."""


class LockedClass:
    """
    LockedClass - A class with restricted attribute creation.

    Attributes:
        first_name: A string representing the first name.
                    It is the only attribute that can be dynamically created.
    """
    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        """
        Initialize a LockedClass instance.

        Parameters:
            first_name (str): The first name (default is None).
        """
        self.first_name = first_name
