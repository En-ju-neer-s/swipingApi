from flask import request, Blueprint, json
from bson.json_util import dumps
from flask_pymongo import MongoClient

title_route = Blueprint('title_route', __name__)

# connect with mongo
client = MongoClient('mongodb://localhost:27017/')

db = client.swiper
# get collectoins
collectionTitles = db.testTitles
binarySet = db.binary


@title_route.route('/', methods=['GET', 'POST'])
def returnTitles():
    if request.method == 'GET':  # return all
        return 'GET ALL THE THE TITLES', 200
    else:  # check for post with userid and everything
        if 'id' in request.json and request.json['id'] != '':
            id = request.json['id']  # id from the post with userid
            if binarySet.find({'userId': id}).count() > 0:
                titlesSeen = list(binarySet.aggregate([  # the list is to transform the cursor to a list
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

                title = collectionTitles.aggregate([
                    {'$match': {'primary_key': {'$nin': titlesSeen}}},
                    {'$sample': {'size': 1}},
                    {'$project': {'title': 1, 'description': 1, 'url': 1, 'primary_key': 1, 'timestamp': 1, '_id': 0}}
                ])
            else:
                title = collectionTitles.aggregate([{'$sample': {'size': 1}}, {'$project': {'title': 1, 'description': 1, 'url': 1, 'primary_key': 1, 'timestamp': 1, '_id': 0}}])

            return dumps(title), 200
        else:
            return 'id not filled', 403
