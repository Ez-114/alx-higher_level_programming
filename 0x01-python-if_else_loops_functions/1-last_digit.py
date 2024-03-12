#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
else:
    last_digit = number % -10

st = "The last digit of {} is {} ".format(number, last_digit)

if last_digit > 5:
    st = st + "and is greater than 5"
elif last_digit == 0:
    st = st + "and is 0"
elif last_digit < 6 and last_digit != 0:
    st = st + "and is less than 6 and not 0"

print(st)
