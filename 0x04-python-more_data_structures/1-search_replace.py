#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """search_replace

    replaces all occurrences of an element by another in a new list.

    Args:
        my_list: passed list
        search: element to replace
        replace: the new element
    Return:
        a list with the replaced element
    """
    return list(map(lambda x: replace if x == search else x, my_list))
