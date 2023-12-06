#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Parameters:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - str or None
    """
    if not a_dictionary:
        return None
    max_key = max(a_dictionary, key=lambda k: a_dictionary[k])
    return max_key
