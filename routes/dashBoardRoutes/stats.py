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
    # Get average swipes based on server
    averageData = db.average.find({})

    for averageData in averageData:
        if averageData['calculate']:
            avergageSwipesServer = math.ceil(db.binary.find({}).count() / db.testTitles.find({}).count())
        else:
            avergageSwipesServer = averageData['staticAverage']
        pass

    stats = {
        'allUser': allUsers,
        'allSwipes': allSwipes,
        'averageSwipes': averageSwipes,
        'calculatedAverage': avergageSwipesServer
    }

    return stats
