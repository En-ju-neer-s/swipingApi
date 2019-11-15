from flask import Blueprint
from flask_pymongo import MongoClient

graph_swipes_route = Blueprint('graph_swipes_route', __name__)

# Connect to mongo
client = MongoClient('mongodb://localhost:27017/')
db = client.swiper


@graph_swipes_route.route('/graphSwipes', methods=['GET'])
def graphSwipes():
    return 'eat a dick'
