from flask import request, Blueprint, json
from bson.json_util import dumps
from flask_pymongo import MongoClient

title_route = Blueprint('title_route', __name__)

# connect with mongo
client = MongoClient('mongodb://localhost:27017/')
db = client.swiper
collectionTitles = db.testTitles
binarySet = db.binary


@title_route.route('/', methods=['GET', 'POST'])
def returnTitles():
    if request.method == 'GET':
        # print(collection.find({}))
        return dumps(collection.find({})), 200
    else:  # check for post with username and everything
        id = request.json['id']  # id from the post with userid
        print(id)
        titles = list(binarySet.aggregate([
            {'$match': {'userId': id}},
            {'$group':
                {
                    '_id': 0,
                    'titleKeys': {
                        '$push': '$primary_key'
                    }
                }
             }
        ]))[0]['titleKeys']  # get only list of key

        print((titles))

        title = collectionTitles.aggregate([
            {'$sample': {'size': 1}},
            {'$project': {'title': 1, 'description': 1, 'url': 1, 'primary_key': 1, '_id': 0}}
        ])

        return dumps(title), 200
