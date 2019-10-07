# swipingApi

A api the have control of all the swipes\

# Requierments

For this project you need python 3.
The packages are:

- Flask
- flask_pymongo
- mongoengine

# How to run the project

In the root of the folder type on your command line `python start.py`. The project will auto change on refresh. The project will run on `http://127.0.0.1:5000`.

# Docker

In the console go to the root of the project. And type `docker build -t (name of your folder):latest .` docker will build the image at this point. The server isnt running yet. After the building is done you type: `docker run -p 5000:5000 (name of your folder):latest`. This will run the server and start everything. the server will run on port 5000.
