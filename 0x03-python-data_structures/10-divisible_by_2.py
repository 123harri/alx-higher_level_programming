#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Return a new list with True or False, indicating whether each integer
    in the original list is a multiple of 2.
    """
    result_list = []

    for num in my_list:
        is_divisible_by_2 = num % 2 == 0

        result_list.append(is_divisible_by_2)

    return result_list
