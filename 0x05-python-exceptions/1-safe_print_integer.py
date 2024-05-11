#!/usr/bin/python3
def safe_print_integer(value):
    """safe_print_integer
    prints a given integer value with exception handling

    Args:
        value: integer value
    Return:
        True -> value is correctly printed
        False -> something wrong happend
    """
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    else:
        return True
