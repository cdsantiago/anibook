"""API routes"""
from flask import request, render_template, make_response
from flask import Blueprint
from flask_security import auth_required
from anibook.models.Anime import Anime
from anibook.models.Profile import Profile, Watching, Completed, Backlogged

api = Blueprint("api", __name__)

@api.post("/redirect/<location>")
def redirect(location):
    """htmx custom redirect"""
   
    response = make_response("response content string")
    
    response.headers["HX-Location"] = "/" + location
    
    return response
    
    
    
    

@api.post("/profile/<int:profile_id>/watchlist")
@auth_required()
def add_to_watchilist(profile_id):
    
    profile = Profile.query.get_or_404(profile_id)
    
    list_type = request.form.get("watchlist")
    
    return f"added to {list_type} watchlist!"


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
