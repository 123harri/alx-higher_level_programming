#!/usr/bin/python3

"""
Base module containing the Base class.
"""


class Base:
    """
    Base class for managing id attribute in future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): If not None, assign it to the id attribute.
                      Otherwise, increment __nb_objects
                      and assign the new value to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
