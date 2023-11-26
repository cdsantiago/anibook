"""API routes"""
from flask import request, render_template, make_response
from flask import Blueprint
from flask_security import auth_required
from anibook.models.Anime import Anime
from anibook.models.Profile import Profile, Completed, Watching, Backlogged
from anibook.models import db

api = Blueprint("api", __name__)


@api.post("/redirect/<location>")
def redirect(location):
    """htmx custom redirect"""

    response = make_response("response content string")

    response.headers["HX-Location"] = "/" + location

    return response


@api.post("/profile/<int:profile_id>/<int:anime_id>/watchlist")
@auth_required()
def add_to_watchilist(profile_id, anime_id):

    profile = Profile.query.get_or_404(profile_id)
    anime = Anime.query.get_or_404(anime_id)

    # Helper method

    def remove_from_other_lists(anime, profile):
        watching = Watching.query.filter_by(profile_id=profile.id).first()
        if watching and anime in watching.anime:
            watching.anime.remove(anime)

        completed = Completed.query.filter_by(profile_id=profile.id).first()
        if completed and anime in completed.anime:
            completed.anime.remove(anime)

        backlogged = Backlogged.query.filter_by(profile_id=profile.id).first()
        if backlogged and anime in backlogged.anime:
            backlogged.anime.remove(anime)

        db.session.commit()

    list_type = request.form.get("watchlist")
    # Call helper method
    remove_from_other_lists(anime, profile)

    if list_type == "completed":

        # Check if existing completed list for user
        if profile.completed:
            completed = profile.completed[0]
        else:
            completed = Completed(profile=profile)
            db.session.add(completed)

        # Check if anime already in completed
        if anime not in completed.anime:
            completed.anime.append(anime)
            db.session.commit()

    if list_type == "watching":
        # Check if existing watching list for user
        if profile.watching:
            watching = profile.watching[0]
        else:
            watching = Watching(profile=profile)
            db.session.add(watching)
        # Check if anime already in watching
        if anime not in watching.anime:
            watching.anime.append(anime)
            db.session.commit()

    if list_type == "backlogged":
        # Check if existing backlogged list for user
        if profile.backlogged:
            backlogged = profile.backlogged[0]
        else:
            backlogged = Backlogged(profile=profile)
            db.session.add(backlogged)
        # Check if anime already in backlogged
        if anime not in backlogged.anime:
            backlogged.anime.append(anime)
            db.session.commit()

    all_completed = []

    for completed in profile.completed:
        all_completed.append(completed.anime)

    all_watching = []

    for watching in profile.watching:
        all_watching.append(watching.anime)

    all_backlogged = []

    for backlogged in profile.backlogged:
        all_backlogged.append(backlogged.anime)

    print("COMPLETED: ", all_completed)
    print("WATCHING: ", all_watching)
    print("BACKLOGGED: ", all_backlogged)

    return f"added to: {list_type}, for profile {profile}"


@api.get("/anime/<int:anime_id>/<title>")
def show_anime_details(anime_id, title):

    anime = Anime.query.get_or_404(anime_id, description="Anime not found")

    return render_template("anime_details.html", anime=anime)


# # Example endpoint to add anime to a user's list
# @app.route('/add_anime_to_list/<int:user_id>/<int:anime_id>/<list_type>', methods=['POST'])
# def add_anime_to_list(user_id, anime_id, list_type):
#     user = User.query.get(user_id)
#     anime = Anime.query.get(anime_id)

#     if not user or not anime:
#         return jsonify({"message": "User or Anime not found"}), 404

#     # Check if the list_type is valid (watching, completed, planning)
#     if list_type not in ['watching', 'completed', 'planning']:
#         return jsonify({"message": "Invalid list type"}), 400

#     # Check if the anime is not already in the user's list
#     if not any(entry.anime_id == anime_id and entry.list_type == list_type for entry in user.anime_lists):
#         new_list_entry = List(user=user, anime=anime, list_type=list_type)
#         db.session.add(new_list_entry)
#         db.session.commit()
#         return jsonify({"message": "Anime added to the list successfully"}), 200
#     else:
#         return jsonify({"message": "Anime is already in the list"}), 200
