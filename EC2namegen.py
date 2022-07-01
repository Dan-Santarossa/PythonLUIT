#!/usr/bin/env python3.7
import random

#Welcome to program
print("Welcome to the EC2 unique name generator")
print("")

#Department check
department = input("Please state your department (marketing, accounting, finops): ")

if (department != 'marketing' and department != 'accounting' and department != 'finops'):
    print ("You are not authorized to use this EC2 name generator. ")
else: 
    amount = int(input("Enter the amount of EC2 instances: "))

def generator(department, amount):
    names = []
    department = department.lower
    
