import boto3
import base64
import json
import os


tablename = os.environ['TABLE_NAME']
dynamo = boto3.client('dynamodb')

def lambda_handler(event, context):
    for record in event['Records']:
        
        payload = base64.b64decode(record["kinesis"]["data"])
        
        json_val = json.loads(payload)

        dynamo.put_item(TableName=tablename, Item={"id":{"S":json_val["id"]},\
        "x":{"S":json_val["x"]},"y":{"S":json_val["y"]},\
        "is_hot":{"S":json_val["is_hot"]}})
