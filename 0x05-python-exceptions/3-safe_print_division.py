#!/usr/bin/python3
def safe_print_division(a, b):
    """safe_print_division
    divides 2 integers and prints the result with exception handling

    Args:
        a: first number
        b: second number
    Return:
        result
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result:", result)
        return result
