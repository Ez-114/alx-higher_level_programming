#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    length = 0
    weighted_number = 0
    weighted_sum = 0
    weighted_avg = 0
    for element in my_list:
        weighted_number = element[0] * element[1]
        length += element[1]
        weighted_sum += weighted_number

    weighted_avg = weighted_sum / length
    return weighted_avg
