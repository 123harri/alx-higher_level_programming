#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Parameters:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division, or None if an exception occurs.
    """
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        pass
    except (TypeError, ValueError):
        return None
    finally:
        print("Inside result: {}".format(result))

    return result
