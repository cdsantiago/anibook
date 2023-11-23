"""user related views"""
from flask import Blueprint
from flask_security import auth_required

user = Blueprint('user', __name__)

@user.route("/profile/<username>")
def render_user_profile(username):
    """render the user profile page"""
    print(username)
    return f"user profile template for user: {username}"
