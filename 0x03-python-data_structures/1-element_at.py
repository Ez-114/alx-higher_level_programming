#!/usr/bin/python3

def element_at(my_list, idx):
    """ element_at

    retrieves an element from alist like in C.

    Args:
        my_list: list passed to the function
        idx: index of the element to be retrieved

    Return:
        The element at the given index `idx`
        `None` if failed
    """

    if idx < 0 or idx > len(my_list):
        return None
    else:
        return my_list[idx]
