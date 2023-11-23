"""List model"""
from . import db
from .Anime import Anime


class List(db.Model):
    """List model"""
    __tablename__ = "lists"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    anime_id = db.Column(db.Integer, db.ForeignKey('anime.id'), nullable=False)
    # 'watching', 'completed', 'planning'
    list_type = db.Column(db.String(20), nullable=False)
    anime = db.relationship('Anime', backref='lists', lazy=True)
