import json


def hello(event, context):
    
    if 'body' in event:
        posted_body = event['body']
    
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": posted_body
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
