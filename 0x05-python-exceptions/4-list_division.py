#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """list_division
    divide elements from list1 and list2 by each other

    Args:
        my_list_1: list 1
        my_list_2: list 2
        list_length: len of list
    Return:
        result list
    """
    i = 0
    div_result = 0
    result = []
    while i < list_length:
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
        except TypeError:
            print("wrong type")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            result.append(div_result)
            i += 1
    return result
