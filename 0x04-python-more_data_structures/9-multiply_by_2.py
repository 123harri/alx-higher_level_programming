#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Parameters:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - dict: A new dictionary with all values multiplied by 2.
    """
    multiplied_dict = {key: value * 2 for key, value in a_dictionary.items()}

    return multiplied_dict
