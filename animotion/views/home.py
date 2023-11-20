"""home related views"""
from flask import Blueprint, render_template_string
from flask_security import auth_required

home= Blueprint('home', __name__)

@home.route("/home")
@auth_required()
def render_home():
    return render_template_string("Hello {{ current_user.email }}")
