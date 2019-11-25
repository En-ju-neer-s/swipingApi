from flask import Blueprint
from flask_pymongo import MongoClient
from bson.json_util import dumps

graph_swipes_route = Blueprint('graph_swipes_route', __name__)

# Connect to mongo
client = MongoClient('mongodb://localhost:27017/')
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
