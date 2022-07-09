import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

title = "Blade Runner 2049"
year = 2017

response = table.update_item(
    Key={
        'year': year,
        'title': title
    },
    UpdateExpression="set #info_rating=:r, #info_plot=:p, #info_actors=:a",
    ExpressionAttributeNames={
        '#info_rating': 'info.rating',
        '#info_plot': 'info.plot',
        '#info_actors': 'info.actors'
    },
    ExpressionAttributeValues={
        ':r': decimal.Decimal(8.0),
        ':p': "Young Blade Runner K's discovery of a long-buried secret leads him to track down former Blade Runner Rick Deckard, who's been missing for thirty years.",
        ':a': ["Harrison Ford", "Ryan Gosling", "Ana de Armas"]
    },
    ReturnValues="UPDATED_NEW"
)

print("UpdateItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))
