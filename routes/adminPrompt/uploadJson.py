import json
import hashlib
import base64
from flask import Blueprint, request
from ..connection import client
from bson.json_util import dumps

upload_route = Blueprint('upload_route', __name__)  # set route

# connect to DB
db = client.swiper


@upload_route.route('/upload', methods=['post'])
def uploadRoute():
    # check if file is present and if it is json
    if request.files['file'] and '.json' in request.files['file'].filename:
        fileInput = request.files['file'].read().decode('utf-8')  # Read file and make it string

        # Check if it is valid json
        try:
            jsonConverted = json.loads(fileInput)
            # Cleaning part of the script
            article = {}
            articles = []
            for jsonObject in jsonConverted:
                # Create the whole object with all the normal items
                article['primary_key'] = hashlib.md5(jsonObject['url'].encode('utf-8')).hexdigest()  # Hashing the url to create the primary key
                article['url'] = jsonObject['url']
                article['title'] = base64.b64encode(bytes(jsonObject['title'], 'utf-8')).decode('utf-8')
                article['description'] = base64.b64encode(bytes(jsonObject['description'], 'utf-8')).decode('utf-8')
                article['og-title'] = base64.b64encode(bytes(jsonObject['og-title'], 'utf-8')).decode('utf-8')
                article['timestamp'] = jsonObject['timestamp']
                articles.append(article)  # append the article to a list of articles

            # upload the json to mongo
            db.fakeTitles.insert(json.loads(dumps(articles)))
        except ValueError as e:
            print(e)
            return dumps({"succes": False, 'errorMessage': 'Json is not correct'}), 404

    return dumps({"succes": true, 'errorMessage': 'corect'}), 202
