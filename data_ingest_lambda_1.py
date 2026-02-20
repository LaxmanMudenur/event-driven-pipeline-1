import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    data = event
    
    file_name = f"data/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.json"
    
    s3.put_object(
        Bucket="event-data-bucket-lucky-cf",
        Key=file_name,
        Body=json.dumps(data)
    )
    
    return {
        "statusCode": 200,
        "body": "Hello from Github Laxman!"
    }
