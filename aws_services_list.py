#!/usr/bin/python

#Create a list of AWS services using Python
#The list should be empty initially
#Populate the list using append or insert
#Print the list and the length of the list
#Remove two specific services from the list by name or by index
#Print the new list and the new length of the list

#empty list
import time
aws_services = []

print("This is an empty list", (aws_services))

time.sleep(2)
#add services to list

print("Adding 10 aws services to list with append")

aws_services.insert(1,'Cognito')
aws_services.insert(2,'S3')
aws_services.insert(3,'Lambda')
aws_services.insert(4,'DynamoDB')
aws_services.insert(5,'EC2')
aws_services.insert(6,'Cloudfront')
aws_services.insert(7,'VPC')
aws_services.insert(8,'RDS')
aws_services.insert(9,'Elasticache')
aws_services.insert(10,'SNS')

#print list and length of list
time.sleep(2)
print(aws_services)
print("How many items in this list?", len(aws_services)) 

import time
time.sleep(2)

#delete two services
print("Say goodbye to two services...")
time.sleep(2)

del aws_services[9]
del aws_services[8]

print("Removed the last two items by index")


#print new list and length of list
print(aws_services)

print("New length of list", len(aws_services)) 