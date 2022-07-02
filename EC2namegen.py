#!/usr/bin/env python3.7
import random
import string

#Welcome to program
print("Welcome to the EC2 unique name generator")
print("")

depts = ['marketing', 'accounting', 'finops']
maxinstances = 1000
mininstances = 1
ec2list = []

#Department check
department = input("Please state your department (Marketing, Accounting, FinOps): ").lower()

if (department not in depts):
    print ("You are not authorized to use this EC2 name generator. ")
else: 
    amount = int(input("Enter the amount of EC2 instances: "))
    if amount > maxinstances:
        print ("Amount of instances to high {}".format(maxinstances))
    elif amount < mininstances:
        print ("Amount of instances to low {}".format(mininstances))
    else:
        
        for instance in range(0, amount):
            randomnum = random.randint(0, 999)
            randomchar = ''.join(random.choices(string.ascii_letters, k=5))
            ec2name = "{}_{}{}{}".format(department, randomnum, randomchar, instance)
            ec2list.append(ec2name)

        print("\n".join(ec2list))
        

def generator():
    depts = ['marketing', 'accounting', 'finops']
    maxinstances = 1000
    mininstances = 1
    ec2list = []
    print("this one")
    #Department check
    department = input("Please state your department (Marketing, Accounting, FinOps): ").lower()
    
    if (department not in depts):
        print ("You are not authorized to use this EC2 name generator. ")
    else: 
        amount = int(input("Enter the amount of EC2 instances: "))
        if amount > maxinstances:
            print ("Amount of instances to high {}".format(maxinstances))
        elif amount < mininstances:
            print ("Amount of instances to low {}".format(mininstances))
        else:
            
            for instance in range(0, amount):
                randomnum = random.randint(0, 999)
                randomchar = ''.join(random.choices(string.ascii_letters, k=5))
                ec2name = "{}_{}{}{}".format(department, randomnum, randomchar, instance)
                ec2list.append(ec2name)
    
            print("\n".join(ec2list))
            
    return ec2list
    
if __name__ == "__main__":
    generator()
    
    
    

