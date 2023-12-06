#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Parameters:
    - set_1 (set): The first set.
    - set_2 (set): The second set.

    Returns:
    - set: A set containing common elements present in both input sets.
    """
    common_elements_set = set_1 & set_2

    return common_elements_set
