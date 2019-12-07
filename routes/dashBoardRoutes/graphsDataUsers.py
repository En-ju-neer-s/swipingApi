
from flask import Blueprint
from bson.json_util import dumps
from ..connection import client

graph_swiper_users = Blueprint('graph_swiper_users', __name__)

# Connect to mongo
db = client.swiper


@graph_swiper_users.route('/graphUsers', methods=['GET'])
def graphUsers():
    totalUsers = db.users.aggregate([
        {"$group":
         {'_id': "$timestamp",
          'count': {'$sum': 1}
          }
         }
    ])

    return dumps(totalUsers)
