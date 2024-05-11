#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as valerr:
        sys.stderr.write("Exception: {}\n".format(valerr))
        return False
    else:
        return True
