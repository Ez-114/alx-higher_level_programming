#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0

    roman_digits = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    decimal_number = 0
    number = 0

    for digit in reversed(roman_string):
        number = roman_digits[digit]
        decimal_number += number if decimal_number < number * 5 else -number
    return decimal_number
