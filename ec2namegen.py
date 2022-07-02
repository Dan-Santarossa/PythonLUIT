#!/usr/bin/env python3.7
import random
import string

#Welcome to program
def generator(department, amount):
    depts = ['marketing', 'accounting', 'finops']
    ec2list = []
    department = department.lower()
    #department check
    if (department not in depts):
        print ("You are not authorized to use this EC2 name generator. ")
    else: #instance name creation
       
        for instance in range(0, amount):
            randomnum = random.randint(100, 999)
            randomchar = ''.join(random.choices(string.ascii_letters, k=5))
            ec2name = "{}_{}{}{}".format(department, randomnum, randomchar, instance)
            ec2list.append(ec2name)
    
        print("\n".join(ec2list)) #print list
            
    return ec2list
    

    
    
    

