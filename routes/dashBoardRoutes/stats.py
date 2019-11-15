from flask import Blueprint
from flask_pymongo import MongoClient
from bson.json_util import dumps


stats_route = Blueprint('stats_route', __name__)  # set route

# Connect met mongo
client = MongoClient('mongodb://localhost:27017/')
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
