"""home related views"""
from flask import Blueprint

home= Blueprint('home', __name__)

@home.route("/home")
def render_home():
    """render the home page"""
    return "home template"
