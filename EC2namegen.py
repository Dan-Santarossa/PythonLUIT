#!/usr/bin/env python3.7
import random

#Welcome to program
print("Welcome to the EC2 unique name generator")
print("")

depts = ['Marketing', 'Accounting', 'Finops']
maxinstances = 1000

x = 'marKeting'
print(x)
y = x
print(y)
z = x.lower()
print(z)
print(x)
print(depts)

#Department check
department = input("Please state your department (marketing, accounting, finops): ")

if (department not in depts):
    print ("You are not authorized to use this EC2 name generator. ")
else: 
    amount = int(input("Enter the amount of EC2 instances: "))
    if amount > maxinstances:
        print ("Amount of instances to high ({}{} Max)".format(maxinstances, x))

#def generator(department, amount):
 #    = []
  #  department = department.lower
    
