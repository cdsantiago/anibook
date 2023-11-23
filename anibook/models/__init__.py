"""models module"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    """anitialize this database"""
    db.init_app(app)
