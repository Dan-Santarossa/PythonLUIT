#Create a list of AWS services using Python
#The list should be empty initially
#Populate the list using append or insert
#Print the list and the length of the list
#Remove two specific services from the list by name or by index
#Print the new list and the new length of the list

#empty list
aws_services = []

print(aws_services)

#add services to list

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

print(aws_services)