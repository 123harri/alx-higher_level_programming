#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Parameters:
    - a_dictionary (dict): The input dictionary.
    - key (str): The key to be deleted.

    Returns:
    - a_dictionary (dict): The modified dictionary after deleting the specified key.
    """
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
