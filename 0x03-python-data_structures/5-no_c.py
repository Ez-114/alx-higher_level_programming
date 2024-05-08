#!/usr/bin/python3

def no_c(my_string):
    noCstr = ""

    for letter in my_string:
        if letter != 'c' and letter != 'C':
            noCstr += letter
    return noCstr
