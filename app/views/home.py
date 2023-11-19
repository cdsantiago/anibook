"""home related views"""
from flask import Blueprint

home= Blueprint('home', __name__)

@home.route("/")
def render_home():
    """render the home page"""
    return "home"
