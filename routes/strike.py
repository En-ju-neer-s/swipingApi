from flask import Blueprint, request
from flask_pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.swiper

strike_route = Blueprint('strike_route', __name__)
@strike_route.route('/', methods=['PATCH'])
def addStrike():
    if request.json:
        if ('userId' in request.json and request.json['userId'] != '' and db.users.find({'userId': request.json['userId']}).count() != 0):

            db.users.update(
                {'userId': request.json['userId']},
                {'$inc': {'strikes': 1}}
            )

            return 'updated-strikes', 201
        else:
            return 'give me a userid', 400
    else:
        return 'WHERE MY BODY AT', 404
