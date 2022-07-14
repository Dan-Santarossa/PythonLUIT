#!/usr/bin/env python3.7
import random
import string
from retry import retry
import getpass
#Welcome to program
print("Welcome to the EC2 unique name generator")
print("")

passwd = ['gimmydaec2']
depts = ['marketing', 'accounting', 'finops']
ec2list = []
maxinstances = 1000
mininstances = 1
#Department input and check
department = input("Please state your department (Marketing, Accounting, FinOps): ").lower()

#If check department unsuccessful print unauthorized message
if (department not in depts):
    print ("You are not authorized to use this EC2 name generator. ")
    
elif (department in depts):
    input("Please enter password: ", getpass(passwd)).lower()

else: 
    amount = int(input("Enter the amount of EC2 instances: "))
    if amount > maxinstances:
        print ("Amount of instances to high {}".format(maxinstances))
    elif amount < mininstances:
        print ("Amount of instances to low {}".format(mininstances))

    else: #if department check successful ask for amount of names
        print("")
    amount = int(input("Enter the amount of EC2 instances: "))
    
    #instance name creation. created instance, randomnum, randomchar, ec2name variables
    for instance in range(0, amount):
        randomnum = random.randint(100, 999)
        randomchar = ''.join(random.choices(string.ascii_letters, k=5))
        ec2name = "{}_{}{}{}".format(department, randomnum, randomchar, instance)
        ec2list.append(ec2name)
        

    print("\n".join(ec2list))
    
