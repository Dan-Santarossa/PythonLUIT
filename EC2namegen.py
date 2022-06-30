#!/usr/bin/env python3.7
import random

print("Welcome to the EC2 unique name generator")
print("")

department = input("Please state your department (marketing, accounting, finops): ")

if (department != 'marketing' and department != 'accounting' and department != 'finops'):
    print ("You are not authorized to use this EC2 name generator. ")
else: 
    print (input("Please enter a number of EC2 instances: "))
        
        
        
        
        



#amount = int(input("Enter the amount of EC2 instances: "))
#if (department == 'marketing' and department == 'accounting' and department == 'finops'):