#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a name exception with a custom message.

    Parameters:
        message (str): Custom message for the exception.

    Raises:
        NameError: Always raises a NameError with the specified message.
    """
    raise NameError(message)
