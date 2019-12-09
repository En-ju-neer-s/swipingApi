from flask import Blueprint
from ..connection import client
from bson.json_util import dumps

stats_route = Blueprint('stats_route', __name__)  # set route

# Connect met collection
db = client.swiper


@stats_route.route('/stats', methods=['GET'])
def stats():
    # Get total users
    allUsers = db.users.find({}).count()
    # Get all swipes
    allSwipes = db.binary.find({}).count()
    # average swipes a person
    averageSwipes = int(allSwipes / allUsers)

    stats = {
        'allUser': allUsers,
        'allSwipes': allSwipes,
        'averageSwipes': averageSwipes
    }

    return stats
