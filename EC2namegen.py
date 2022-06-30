#!/usr/bin/env python3.7

import random


department = input("Please state your Department (marketing, accounting, finops): ")
amount = int(input("Enter the amount of EC2 instances:" ))

for dept in department:    
    if (department != 'marketing' and department != 'accounting' and department != 'finops'):
        print ("You are not authorized to use this EC2 name generator.")
        exit()
    
    elif (department == 'marketing' and department == 'accounting' and department == 'finops'):
        print (input("Please enter a number of EC2 instances. "))
        