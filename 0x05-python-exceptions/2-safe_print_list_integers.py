#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x integers in a list.

    Parameters:
        my_list (list): The input list.
        x (int): The number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.
    """
    printed_integers = 0

    try:
        for i in range(x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end=" ")
                printed_integers += 1
    except (IndexError, ValueError, TypeError):
        pass
    print()
    return printed_integers
