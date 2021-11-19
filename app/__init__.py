from flask import Flask
from app.view import route_views


def create_app():
    app = Flask(__name__)
    route_views.init_app(app)
    return app
