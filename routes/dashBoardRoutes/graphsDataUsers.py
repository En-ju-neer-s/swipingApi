
from flask import Blueprint
from flask_pymongo import MongoClient

graph_swiper_users = Blueprint('graph_swiper_users', __name__)

# Connect to mongo
client = MongoClient('mongodb://localhost:27017/')
db = client.swiper


@graph_swiper_users.route('graphUsers', methods=['GET'])
def graphUsers():
    return 'eat morks pielemuis'
