import os

from flask import Flask
from flask_cors import CORS, cross_origin
from random import randrange
import simplejson as json
import boto3
from multiprocessing import Pool
from multiprocessing import cpu_count

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"Access-Control-Allow-Origin": "*"}})

ddb_aws_region = os.getenv('DDB_AWS_REGION', "us-west-2")
ddb_table_name = os.getenv('DDB_TABLE_NAME', "restaurants-voting-app")

ddb = boto3.resource('dynamodb', region_name=ddb_aws_region)
ddbtable = ddb.Table(ddb_table_name)

def readvote(restaurant):
    response = ddbtable.get_item(Key={'name': restaurant})
    # this is required to convert decimal to integer 
    normilized_response = json.dumps(response)
    json_response = json.loads(normilized_response)
    votes = json_response["Item"]["restaurantcount"]
    return str(votes)

def updatevote(restaurant, votes):
    ddbtable.update_item(
        Key={
            'name': restaurant
        },
        UpdateExpression='SET restaurantcount = :value',
        ExpressionAttributeValues={
            ':value': votes
        },
        ReturnValues='UPDATED_NEW'
    )
    return str(votes)


@app.route('/')
def home():
    html = "<h1>Welcome to the Voting App</h1><p><b>To vote, you can call the following APIs:</b></p><p>/api/restaurant-1</p><p>/api/restaurant-2</p><p>/api/restaurant-3</p><p>/api/restaurant-4</p><b>To query the votes, you can call the following APIs:</b><p>/api/getvotes</p>"
    return {
        "statusCode": 200,
        "body": html,
        "headers": {
            "Content-Type": "text/html"
        }
    }

@app.route("/api/restaurant-1")
def restaurant1():
    string_votes = readvote("restaurant-1")
    votes = int(string_votes)
    votes += 1
    string_new_votes = updatevote("restaurant-1", votes)
    return {
        "statusCode": 200,
        "body": string_new_votes 
    }

@app.route("/api/restaurant-2")
def restaurant2():
    string_votes = readvote("restaurant-2")
    votes = int(string_votes)
    votes += 1
    string_new_votes = updatevote("restaurant-2", votes)
    return {
        "statusCode": 200,
        "body": string_new_votes 
    }

@app.route("/api/restaurant-3")
def restaurant3():
    string_votes = readvote("restaurant-3")
    votes = int(string_votes)
    votes += 1
    string_new_votes = updatevote("restaurant-3", votes)
    return {
        "statusCode": 200,
        "body": string_new_votes 
    }

@app.route("/api/restaurant-4")
def restaurant4():
    string_votes = readvote("restaurant-4")
    votes = int(string_votes)
    votes += 1
    string_new_votes = updatevote("restaurant-4", votes)
    return {
        "statusCode": 200,
        "body": string_new_votes 
    }

@app.route("/api/getvotes")
def getvotes():
    string_restaurant1 = readvote("restaurant-1")
    string_restaurant2 = readvote("restaurant-2")
    string_restaurant3 = readvote("restaurant-3")
    string_restaurant4 = readvote("restaurant-4")
    
    string_votes = '[{"name": "restaurant-1", "value": ' + string_restaurant1 + '},' + '{"name": "restaurant-2", "value": ' + string_restaurant2 + '},' + '{"name": "restaurant-3", "value": '  + string_restaurant3 + '}, ' + '{"name": "restaurant-4", "value": '  + string_restaurant4 + '}]'
    return {
        "statusCode": 200,
        "body": string_votes
    }

if __name__ == '__main__':
   app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
   app.debug =True

def lambda_handler(event, context):
    path = event.get('rawPath', '/')
    
    if path == '/':
        response = home()
    elif path == '/api/getvotes':
        response = getvotes()        
    elif path == '/api/restaurant-1':
        response = restaurant1()
    elif path == '/api/restaurant-2':
        response = restaurant2()
    elif path == '/api/restaurant-3':
        response = restaurant3()
    elif path == '/api/restaurant-4':
        response = restaurant4()
    else:
        response = {
            "statusCode": 404,
            "headers": {"Content-Type": "text/html"},
            "body": "<h1>404 Not Found</h1>",
        }
    
    return response
