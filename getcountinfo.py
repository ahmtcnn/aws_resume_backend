import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
 
  table = dynamodb.Table('countertable')
  response = table.scan()
  data = response['Items']


 
  return data
