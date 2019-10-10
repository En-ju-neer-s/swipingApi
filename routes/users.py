from flask import Blueprint, request
from flask_pymongo import MongoClient
from bson.json_util import dumps

users_route = Blueprint('users_route', __name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.swiper
collection = db.binary


@users_route.route('/', methods=['GET'])
def topUsers():
    if request.method == 'GET':

        topTen = collection.aggregate([
            {
                '$group': {
                    '_id': '$userId',
                    'count': {'$sum': 1}
                }},
            {'$sort': {'count': -1}},
            {'$limit': 10}
        ])

        return dumps(topTen), 201
