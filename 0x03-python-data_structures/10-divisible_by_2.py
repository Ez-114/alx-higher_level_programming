#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    return [item % 2 == 0 for item in my_list]
