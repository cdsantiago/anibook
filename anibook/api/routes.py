"""API routes"""
from flask import request
from flask import Blueprint

api = Blueprint('api', __name__)

@api.route("/add_anime_to_list", methods=["POST", "GET"])
def add_anime_to_list():
    
    if request.method == "GET":
        return "add anime to list"




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
