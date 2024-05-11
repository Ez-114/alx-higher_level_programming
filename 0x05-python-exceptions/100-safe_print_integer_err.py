#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as valerr:
        sys.stderr.write("Exception: {}\n".format(valerr))
        return False
    except TypeError as typerr:
        sys.stderr.write("Exception: {}\n".format(typerr))
        return False
    else:
        return True
