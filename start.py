import os
from flask import Flask, json, url_for
# Swiper Routes
from routes.swipes import swipe_route
from routes.user import user_route
from bson.json_util import dumps
from routes.users import users_route
from routes.strike import strike_route
from routes.title import title_route
from routes.fakeArticles import fake_route
# Dashboard Router
from routes.dashBoardRoutes.stats import stats_route
from routes.dashBoardRoutes.graphsDataSwipes import graph_swipes_route
from routes.dashBoardRoutes.graphsDataUsers import graph_swiper_users
from routes.dashBoardRoutes.swipesStats import swipesStats
# admin routes
from routes.adminPrompt.uploadJson import upload_route
from routes.adminPrompt.getNewsSources import news_source_route
# Mongo imports
from flask_pymongo import PyMongo  # connect to mongo DB
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Setup the mongoDB
app.config["MONGO_DBNAME"] = "swiper"
app.config["MONGO_URI"] = "mongodb://localhost:27017/swiper"
# Add mongo to server
mongo = PyMongo(app)

# register routes
app.register_blueprint(swipe_route, url_prefix='/swipe')
app.register_blueprint(user_route, url_prefix='/user')
app.register_blueprint(users_route, url_prefix='/users')
app.register_blueprint(title_route, url_prefix='/title')
app.register_blueprint(strike_route, url_prefix='/strike')
# Dasboard routes
app.register_blueprint(stats_route, url_prefix='/dashboard')
app.register_blueprint(graph_swipes_route, url_prefix='/dashboard')
app.register_blueprint(graph_swiper_users, url_prefix='/dashboard')
app.register_blueprint(swipesStats, url_prefix='/dashboard')
app.register_blueprint(fake_route, url_prefix='/fakeRoute')
# Admin routes
app.register_blueprint(upload_route, url_prefix='/admin')
app.register_blueprint(news_source_route, url_prefix='/admin')

# initial route
@app.route('/')
def hello_world():
    return dumps({
        "made by": "This api is made by the enjuneers in assignment of ACED.",
        "Creators": {
            "frontend": [
                "Robin Treur, robintreur@gmail.com",
                "Mark Vonk, markjhvonk@gmail.com"
            ],
            "backend": "Roel Voordendag, rvoordendag@gmail.com"
        },
        "routes": [
            "/user, POST",
            "/users, GET",
            "/title, POST",
            "/swipe, POST",
            "/strike, PUT",
        ],
        'routes dashboard': [
            '/dashBoard',
            '/graphSwipes Swipes, Get all swipes with date',
            '/graphUsers, Get all swipes with users and data',
            '/stats, get the general stats'
            '/swipesStats stats for the main item'
        ]
    })


if __name__ == "__main__":
    app.run(use_reloader=True)
    # app.run(host='0.0.0.0', debug=True)
    # app.run()
