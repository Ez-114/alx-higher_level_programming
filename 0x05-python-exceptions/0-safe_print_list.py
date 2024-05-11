#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """safe_print_list
    prints x elements from a given list

    Args:
        my_list: passed list of elements
        x: tells how much elements to print from the given list `my_list`

    Return:
        total successfuly printed elements from `my_list`
    """
    score = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            score += 1
        except IndexError:
            break
    print()
    return (score)
