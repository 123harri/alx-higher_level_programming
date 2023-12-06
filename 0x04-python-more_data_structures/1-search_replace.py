#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Parameters:
    - my_list (list): The initial list.
    - search: The element to replace in the list.
    - replace: The new element.

    Returns:
    - list: A new list with all occurrences of 'search' replaced by 'replace'.
    """
    new_list = []

    for element in my_list:
        new_element = replace if element == search else element
        new_list.append(new_element)

    return new_list
