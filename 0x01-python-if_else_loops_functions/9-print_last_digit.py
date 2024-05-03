#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    mod = number % 10
    print("{}".format(mod), end='')
    return (mod)
