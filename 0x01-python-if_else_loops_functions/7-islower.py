#!/usr/bin/python3
def islower(c):
    '''
        check if the passed character is lower case
    '''
    return True if ord(c) >= 97 and ord(c) <= 122 else False
