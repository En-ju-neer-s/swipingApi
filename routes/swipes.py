# File to fix count the swipes
from flask import Blueprint, request
from flask_pymongo import MongoClient


# connect to mongo
client = MongoClient('mongodb://localhost:27017/')
db = client.swiper

swipe_route = Blueprint('swipe_route', __name__)
@swipe_route.route('/', methods=['GET', 'POST'])
def swipes():
    if request.method == 'POST':

        if ('userId' in request.json and request.json['userId'] != '') and ('primaryKey' in request.json and request.json['primaryKey'] != '') and ('clickbait' in request.json and type(request.json['clickbait']) == int):
            binaryObject = {}
            for objectName in request.json:
                binaryObject[objectName] = request.json[objectName]
                pass

            db.binary.insert_one(binaryObject)

            return 'saved', 201
        else:
            return 'POST OBJECT NOT RIGHT', 403
    else:
        return 'Welcome to the get'
