class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Raise an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer and greater than 0.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        super().__init__()  # Call the constructor of the base class
        self.__width = 0
        self.__height = 0
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
