"""home related views"""
from flask import Blueprint, render_template
from anibook.models.Anime import Anime

index = Blueprint('index', __name__)


@index.route("/")
def render_index():
    
    top_ranked_anime = Anime.query.filter(
        Anime.rank > 0, Anime.rank < 38, Anime.media_type == 'tv').order_by((Anime.rank)).all()
    
    return render_template("index.html", top_ranked_anime=top_ranked_anime)


