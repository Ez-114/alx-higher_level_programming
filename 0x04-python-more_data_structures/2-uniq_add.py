#!/usr/bin/python3
def uniq_add(my_list=[]):
    """uniq_add

    adds all unique integers in a list

    Args:
        my_list: passed list
    Return:
        sum of all unique numbers in a list
    """

    # Handel if my_list is empty
    if not my_list:
        return 0

    summs = 0
    for i in set(my_list):
        summs += i

    return summs
