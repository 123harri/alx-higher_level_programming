#!/usr/bin/python3
def safe_function(fct, *args):
    """
    Executes a function safely.

    Parameters:
        fct (function): A pointer to the function to be executed.
        *args: Variable number of arguments to be passed to the function.

    Returns:
        The result of the function.
        Returns None if an exception occurs, and prints the error in stderr.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
