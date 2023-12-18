#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists.

    Parameters:
        my_list_1 (list): The first input list.
        my_list_2 (list): The second input list.
        list_length (int): The length of the new list.

    Returns:
        list: A new list with all divisions.
    """
    result_list = []

    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except (TypeError, ValueError):
                print("wrong type")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            finally:
                result_list.append(result)
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        return result_list
