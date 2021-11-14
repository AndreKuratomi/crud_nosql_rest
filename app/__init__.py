from flask import Flask
from app.view import route_views
from ipdb import set_trace


# set_trace()
def create_app():
    app = Flask(__name__)
    route_views.init_app(app)
    return app
