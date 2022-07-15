import boto3

sns = boto3.client("sns",
                  region_name="us-east-1")

response = sns.create_topic(Name="Project15_sns")
topic_arn = response["TopicArn"]

print(topic_arn)

# response = sns.subscribe(TopicArn=topic_arn,
#                          Protocol="email",
#                          Endpint="dpsantarossa@gmail.com")

