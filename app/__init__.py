"""app module"""
from flask import Flask
from .views.home import home


def create_app():
    """create app"""
    app = Flask(__name__)
    
    #Register Blueprints
    app.register_blueprint(home)

    return app
