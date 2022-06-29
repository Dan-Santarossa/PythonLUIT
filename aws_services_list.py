#!/usr/bin/env python3.7

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

print("Adding 10 aws services")

aws_services += ('Cognito', 'S3', 'Lambda', 'DynamoDB', 'EC2','Cloudfront','VPC','RDS','Elasticache','SNS')

#print list and length of list
time.sleep(2)
print(aws_services)
print("How many items in this list?", len(aws_services)) 

time.sleep(2)

#delete two services
print("Say goodbye to two services...")
time.sleep(2)

del aws_services[9]
del aws_services[8]

print("Removed the last two items by index")
time.sleep(2)

#print new list and length of list
print("New list of services", (aws_services))

print("New length of list:", len(aws_services)) 

