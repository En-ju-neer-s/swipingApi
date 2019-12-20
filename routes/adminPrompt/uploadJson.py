import json
import hashlib
import datetime
import base64
from hashlib import sha256
from flask import Blueprint, request
from ..connection import client
from bson.json_util import dumps

upload_route = Blueprint('upload_route', __name__)  # set route

# connect to DB
db = client.swiper

# TODO: ADD PASSWORD HANDLER FOR POSTING IT


@upload_route.route('/upload', methods=['post'])
def uploadRoute():
    # check if file is present and if it is json
    print(list(db.apiKey.find({'apiKey': request.form['apiKey']})))
    if db.apiKey.find({'apiKey': request.form['apiKey']}).count() > 0:
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

                    # Write validation to look if source is already in script and after that
                    if request.form['source'] and len(request.form['source']) > 0:  # Validation
                        allSources = list(db.newsProviders.find({}))  # All the news sources
                        for source in allSources:
                            if source['name'] != request.form['source']:
                                addToDb = True
                        # If addToDb is true add it to the db
                        if addToDb:
                            db.newsProviders.insert_one({'name': request.form['source'], 'value': request.form})

                        article['source'] = request.form['source']

                    articles.append(article)  # append the article to a list of articles

                # Insert into DB when data was uploaded
                db.uploadLogs.insert_one({'user': request.form['username'], 'apiKey': request.form['apiKey']})

                # upload the json to mongo
                db.fakeTitles.insert(json.loads(dumps(articles)))
            except ValueError as e:
                print(e)
                return dumps({"succes": False, 'errorMessage': 'Json is not correct'}), 404

        return dumps({"succes": True, 'errorMessage': 'correct json uploaded'}), 202
    else:
        return dumps({"succes": False, 'errorMessage': 'Api key expired get a new one'}), 301
