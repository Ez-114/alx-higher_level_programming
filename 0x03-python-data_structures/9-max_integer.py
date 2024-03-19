#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    max_num = my_list[0]
    for item in my_list:
        if item > max_num:
            max_num = item
    return (max_num)
