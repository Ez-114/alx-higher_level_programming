#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10 if number > 10 else number % -10
print("Last digit of {:d} is {:d}".format(number, mod), end=' ')
if mod > 5:
    print("and is grater than 5")
elif mod == 0:
    print("and is 0")
elif mod < 6 and mod != 0:
    print("and less than 6 and not 0")
