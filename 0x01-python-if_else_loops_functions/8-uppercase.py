#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print("{:c}".format(ord(char) - 32 if ord(char) in range(97, 123)
                            else ord(char)), end="")
    print()
