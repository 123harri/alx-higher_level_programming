#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Prints an integer and returns True if the value has been correctly printed.
    Otherwise, returns False and prints the error in stderr.

    Parameters:
        value: The input value.

    Returns:
        bool: True if the value is an integer and has been correctly printed,
              False otherwise.
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True
