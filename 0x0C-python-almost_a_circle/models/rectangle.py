#!/usr/bin/python3

"""
Rectangle module containing the Rectangle class.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class inheriting from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X coordinate of the rectangle.
            y (int): Y coordinate of the rectangle.
            id (int): If not None, assign it to the id attribute.
                      Otherwise, increment __nb_objects and assign the new value to the id attribute.
        """
        super().__init__(id)
        self.validate_integer("width", width)
        self.validate_integer("height", height)
        self.validate_integer("x", x, eq=False)
        self.validate_integer("y", y, eq=False)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.

        Args:
            value (int): Value to set for width.
        """
        self.validate_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.

        Args:
            value (int): Value to set for height.
        """
        self.validate_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute.

        Args:
            value (int): Value to set for x.
        """
        self.validate_integer("x", value, eq=False)
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute.

        Args:
            value (int): Value to set for y.
        """
        self.validate_integer("y", value, eq=False)
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance with the character #, taking into account x and y.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: String representation of the Rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """
        Update attributes of the Rectangle instance based on arguments.

        Args:
            *args: Arguments to update attributes in order (id, width, height, x, y).
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
