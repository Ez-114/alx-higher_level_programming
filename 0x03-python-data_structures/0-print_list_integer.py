#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """ print_list_integer:
    print all integers in a list

    Arg:
        my_list - passed list to the function
    """
    for item in my_list:
        print("{:d}".format(item))
