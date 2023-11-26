"""anibook application module"""
from flask import Flask
from pandas import pandas as pd
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail

# views and their blueprints
from .views.home import home
from .views.profile import profile
from .views.index import index

# routes and their blueprints
from .api.routes import api

# models
from .models import db
from .models.Profile import Profile, Role, Watching, Completed, Backlog
from .models.Anime import Anime

# config module
from config import *


def init_app(app):
    """anitialize this database"""
    db.init_app(app)


def create_app():
    """create and configure the application"""
    anibook = Flask(__name__)

    # configurations file
    anibook.config.from_object("config")

    db.init_app(anibook)

    # flask_mail
    mail = Mail(anibook)
    mail.init_app(anibook)

    # flask_security
    user_datastore = SQLAlchemyUserDatastore(db, Profile, Role)
    anibook.security = Security(anibook, user_datastore)

    # register view blueprints
    anibook.register_blueprint(index)
    anibook.register_blueprint(profile, url_prefix="/profile")
    anibook.register_blueprint(home)
    # register api blueprint
    anibook.register_blueprint(api, url_prefix="/api")

    # create all tables
    with anibook.app_context():
        db.create_all()

    return anibook


def import_csv_data_no_ids():
    """import csv"""
    df = pd.read_csv("anime_no_ids.csv")

    df["num_episodes"] = pd.to_numeric(df["num_episodes"], errors="coerce")

    # Convert the 'start_date' column to datetime data type
    df["start_date"] = pd.to_datetime(df["start_date"], format="mixed", dayfirst=True)

    df["end_date"] = pd.to_datetime(df["end_date"], format="mixed", dayfirst=True)

    df["mean"] = pd.to_numeric(df["mean"], errors="coerce")

    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")

    df["rank"] = pd.to_numeric(df["rank"], errors="coerce")

    df["start_season_year"] = pd.to_numeric(df["start_season_year"], errors="coerce")

    df.to_sql("anime", "postgresql:///anibook", if_exists="append", index=False)
