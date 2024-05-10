#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy_dict = a_dictionary.copy()
    for key in cpy_dict:
        cpy_dict[key] *= 2
    return cpy_dict
