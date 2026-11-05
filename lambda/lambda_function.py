#1 Import boto3 and create client connection with bedrock
import boto3
import json
client_sme = boto3.client('bedrock-runtime')

def lambda_handler(event, context):

    #2 a. Store the input in a variable, b. print the event
    user_input = event['prompt']
    print(user_input)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
