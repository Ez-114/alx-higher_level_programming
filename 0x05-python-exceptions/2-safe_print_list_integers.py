#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """safe_print_list_integers
    print x elements form a given list with exception handling

    Args:
        my_list: list of elements
        x: number of elements to print
    Return:
        successfully printed elements
    """
    score = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            score += 1
        except (ValueError, TypeError):
            pass
    print()
    return score
