#!/usr/bin/env python3.7

#python implementation goes here

fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted? "))

#calculation formula

celsius = (fahrenheit - 32) * 5 / 9

print(fahrenheit, "F is", round(celsius, 2), "C")