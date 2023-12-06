#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value in a dictionary.

    Parameters:
    - a_dictionary (dict): The input dictionary.
    - key (str): The key to replace or add.
    - value: The value associated with the key.

    Returns:
    - a_dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
