from flask import Blueprint
from flask_pymongo import MongoClient
from bson.json_util import dumps

swipesStats = Blueprint('swipesStats', __name__)

# Connect to mongo
client = MongoClient('mongodb://localhost:27017/')
db = client.swiper


@swipesStats.route('/swipesStats', methods=['GET'])
def swipesStatsGetter():
    # Get all iitems with how many yesses and nos
    totalSwipes = db.testTitles.aggregate([
        {
            '$lookup': {
                'from': "binary",
                'localField': "primary_key",
                'foreignField': "primaryKey",
                'as': "binaryData"
            }
        },
        {
            '$project': {'title': 1, 'description': 1, 'url': 1, 'primary_key': 1, 'timestamp': 1, '_id': 0, 'binaryData.clickbait': 1}
        },
        {'$group': {
            '_id': "$binary",
            'title': {'$first': '$title'},
            'description': {'$first': '$description'},
            'url': {'$first': '$url'},
            'primary_key': {'$first': '$primary_key'},
            'timestamp': {'$first': '$timestamp'},
            'count': {'$sum': 1}
        }}
    ])

    return dumps(totalSwipes)
