from flask import Blueprint, request
from bson.json_util import dumps
from .connection import client

users_route = Blueprint('users_route', __name__)
# setup connection
db = client.swiper
collection = db.binary


@users_route.route('/', methods=['GET'])
def topUsers():
    if request.method == 'GET':
        topTen = collection.aggregate([
            {
                '$group': {  # Group them together based on userId
                    '_id': '$userId',
                    'username': '$username',
                    'count': {'$sum': 1}  # count per user
                }},
            {'$sort': {'count': -1}},  # return them descending
            {'$limit': 10}
        ])

        return dumps(topTen), 201
