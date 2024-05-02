#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            upper_char = chr(ord(c) - ord('a') + ord('A'))
        else:
            upper_char = c
        result += upper_char
    print("{}".format(result))
