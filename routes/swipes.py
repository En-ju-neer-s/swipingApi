# File to fix count the swipes
from flask import Blueprint, request
from flask_pymongo import MongoClient
from ..config import config

# connect to mongo
client = MongoClient('mongodb://localhost:27017/',
                     username=config.username,
                     passsword=config.password)
db = client.swiper

swipe_route = Blueprint('swipe_route', __name__)
@swipe_route.route('/', methods=['POST'])
def swipes():
    if request.method == 'POST':
        # Basis validation for the request
        if ('userId' in request.json and request.json['userId'] != '') and ('primaryKey' in request.json and request.json['primaryKey'] != '') and ('clickbait' in request.json and type(request.json['clickbait']) == int):
            # more validiont
            if db.users.find({'userId': request.json['userId']}).count() == 0 or db.testTitles.find({'primary_key': request.json['primaryKey']}).count() == 0:
                return 'not found', 404

            binaryObject = {}
            # full the object with all the data
            for objectName in request.json:
                binaryObject[objectName] = request.json[objectName]
                pass
            # insert into the DB
            db.binary.insert_one(binaryObject)

            return 'saved', 201
        else:
            return 'POST OBJECT NOT RIGHT', 403
