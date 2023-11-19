"""app module"""
from flask import Flask
# views
from .views.home import home
from .views.user import user
# models


def create_app():
    """create and configure the app"""
    animotion = Flask(__name__)

    # Load configuration from config.py
    animotion.config.from_pyfile('../config.py')

    # Register Blueprints
    animotion.register_blueprint(home)
    animotion.register_blueprint(user, url_prefix='/user')

    return animotion
