#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Parameters:
    - set_1 (set): The first set.
    - set_2 (set): The second set.

    Returns:
    - set: A set containing elements that are present in only one of the input sets.
    """
    only_diff_elements_set = set_1 ^ set_2

    return only_diff_elements_set
