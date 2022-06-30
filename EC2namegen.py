#!/usr/bin/env python3.7

import random

department = input("What is your Department? (marketing, accounting, finops): ")

for dept in department:    
    if (department != 'marketing' and department != 'accounting' and department != 'finops'):
        print ("You are not authorized to use this EC2 name generator.")
    
    
    else: 
        if (department == 'marketing' and department == 'accounting' and department == 'finops'):
            print (input("Please enter a number of EC2 instances. "))