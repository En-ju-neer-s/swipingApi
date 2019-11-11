from flask import Blueprint, request
from flask_pymongo import MongoClient
from bson.json_util import dumps
from ..config import config

users_route = Blueprint('users_route', __name__)

client = MongoClient('mongodb://localhost:27017/',
                     username=config.username,
                     passsword=config.password)
db = client.swiper
collection = db.binary


@users_route.route('/', methods=['GET'])
def topUsers():
    if request.method == 'GET':
        topTen = collection.aggregate([
            {
                '$group': {  # Group them together based on userId
                    '_id': '$userId',
                    'count': {'$sum': 1}  # count per user
                }},
            {'$sort': {'count': -1}},  # return them descending
            {'$limit': 10}
        ])

        return dumps(topTen), 201
