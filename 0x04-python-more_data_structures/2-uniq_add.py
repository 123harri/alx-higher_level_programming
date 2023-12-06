#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    Parameters:
    - my_list (list): The input list.

    Returns:
    - int: The sum of all unique integers in the list.
    """
    unique_integers = set()
    for element in my_list:
        unique_integers.add(element)
        result_sum = sum(unique_integers)
        return result_sum
