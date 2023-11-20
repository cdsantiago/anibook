"""home related views"""
from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route("/")
def render_index():
    return render_template("index.html")
