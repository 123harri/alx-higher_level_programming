#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer using "{:d}".format().

    Parameters:
        value: The input value.

    Returns:
        bool: True if the value has been correctly printed,
              False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
