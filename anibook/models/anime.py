"""Anime model"""
from datetime import datetime
from . import db


class Anime(db.Model):
    """Anime model"""

    __tablename__ = "anime"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(30))
    media_type = db.Column(db.String(30))
    num_episodes = db.Column(db.Integer())
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    mean = db.Column(db.Float())
    source = db.Column(db.String(30))
    popularity = db.Column(db.Integer())
    rank = db.Column(db.Integer())
    rating = db.Column(db.String(30))
    start_season_year = db.Column(db.Integer())
    start_season_season = db.Column(db.String(30))
    genres = db.Column(db.String())
    studios = db.Column(db.String())
    synopsis = db.Column(db.Text())
    nsfw = db.Column(db.String(30))
    main_picture_medium = db.Column(db.String(), unique=True)
    main_picture_large = db.Column(db.String(), unique=True)
    alternative_titles_en = db.Column(db.String())
    alternative_titles_ja = db.Column(db.String())
    alternative_titles_synonyms = db.Column(db.String())
    created_at = db.Column(db.Date(), default=datetime.utcnow)
    
    def __repr__(self):
        return f"Anime('{self.title}')"
    
    

    
    
