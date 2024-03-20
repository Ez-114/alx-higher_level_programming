#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return (None)
    divBy2 = []
    for item in my_list:
        if item % 2 == 0:
            divBy2.append(True)
        else:
            divBy2.append(False)
    return (divBy2)
