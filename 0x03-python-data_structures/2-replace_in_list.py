#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replace_in_list

    replaces an element of a list at a specific position (like in C)

    Args:
        my_list: passed list
        idx: index of the element to be replaced
        element: new value of old element at index `idx`

    Return:
        Original list if Fails
        Modified copy of OG list
    """

    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    mod_list = my_list[:]
    mod_list[idx] = element
    return mod_list
