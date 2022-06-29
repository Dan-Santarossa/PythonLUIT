#!/usr/bin/env python3.7

import random

department = input("What is your Department? (marketing, accounting, finops): ")
    
if (department != 'marketing' and department != 'accounting' and department != 'finops'):
    print ("You are not authorized to use this EC2 name generator.")

    elif(department == 'marketing' and department == 'accounting' and department == 'finops'):
    print ("Please enter a number of EC2 instances" )