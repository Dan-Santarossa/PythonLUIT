#!/usr/bin/env python3.7
import random
import string

#Welcome to program

print("Welcome to the EC2 unique name generator")
print("")

depts = ['marketing', 'accounting', 'finops']
#maxinstances = 1000
#mininstances = 1
ec2list = []

#Department check
department = input("Please state your department (Marketing, Accounting, FinOps): ").lower()


if (department not in depts):
    print ("You are not authorized to use this EC2 name generator. ")
else: 
    
    amount = int(input("Enter the amount of EC2 instances: "))
    
    for instance in range(0, amount):
        randomnum = random.randint(100, 999)
        randomchar = ' '.join(random.choices(string.ascii_letters, k=5))
        ec2name = "{}_{}{}{}".format(department, randomnum, randomchar, instance)
        ec2list.append(ec2name)
        
        print("\n".join(ec2list))
        
        
        
        #if amount > maxinstances:
    #    print ("Max amount of instances is {}".format(maxinstances))
    #elif amount < mininstances:
    #    print ("Minimum amount of instance is 1 {}".format(mininstances))
    #else: