from flask import Flask
from routes.swipes import swipe_route

app = Flask(__name__)

#register routes
app.register_blueprint(swipe_route, url_prefix='/swipe')

@app.route('/')
def hello_world():
    return 'Welcome at the swiping api.'

if __name__ == "__main__":
    app.run(use_reloader=True)