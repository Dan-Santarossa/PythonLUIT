#!/usr/bin/env python3.7

upper_number = int(input("How many values should we process?: "))

for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)