"""user related views"""
from flask import Blueprint
from flask_security import auth_required

profile = Blueprint("user", __name__)


@profile.route("/<username>")
def get_user_profile(username):
    """render the user profile page"""

    return f"user profile template for user: {username}"
