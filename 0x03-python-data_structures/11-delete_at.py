#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list.
    If idx is negative or out of range, nothing changes (returns the same list).
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]

        my_list.pop()

        return my_list.copy()
