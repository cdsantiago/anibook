"""user related views"""
from flask import Blueprint, render_template
from anibook.models.Anime import Anime
from anibook.models import db
from anibook.models.Profile import Profile
from flask_security import auth_required

profile = Blueprint("user", __name__)


def get_all(list):
    result = []
    for anime in list[0].anime:
        result.append(anime)
    return result


@profile.get("/<username>")
def show_user_profile(username):
    """render the profile page"""
    profile = Profile.query.filter_by(username=username).first()

    completed = get_all(profile.completed)

    watching = get_all(profile.watching)

    backlogged = get_all(profile.backlogged)

    return render_template("profile.html", completed=completed, watching=watching, backlogged=backlogged, username=username)
