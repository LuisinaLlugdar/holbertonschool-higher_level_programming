#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
str = "and is less than 6 and not 0"
if last_digit > 5:
    str = "and is greater than 5"
elif last_digit == 0:
    str = "and is 0"
print(f"The last digit of {number} is {last_digit} {str}")
