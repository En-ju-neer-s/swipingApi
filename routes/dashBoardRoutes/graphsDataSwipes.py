from flask import Blueprint
from flask_pymongo import MongoClient
from bson.json_util import dumps
from ..connection import client

graph_swipes_route = Blueprint('graph_swipes_route', __name__)

# Connect to collection
db = client.swiper


@graph_swipes_route.route('/graphSwipes', methods=['GET'])
def graphSwipes():
    totalSwipes = db.binary.aggregate([
        {"$group":
            {'_id': "$timestamp",
                'count': {'$sum': 1}
             }
         }
    ])

    return dumps(totalSwipes)
