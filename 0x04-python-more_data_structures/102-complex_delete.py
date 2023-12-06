#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.

    Parameters:
    - a_dictionary (dict): The input dictionary.
    - value: The value to search for and delete.

    Returns:
    - a_dictionary
    """
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]
    return (a_dictionary)
