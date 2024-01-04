#!/usr/bin/python3

def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if size is a float.
        ValueError: If size is less than 0.
    """
    # Validate input type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Validate input value
    if size < 0 or isinstance(size, float):
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
