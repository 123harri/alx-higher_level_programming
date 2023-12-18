#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Parameters:
        my_list (list): The input list.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    printed_elements = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_elements += 1
    except IndexError:
        pass
    print()
    return printed_elements
