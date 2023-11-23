"""anibook application module"""
from flask import Flask
from pandas import pandas as pd
import numpy as np
import sqlalchemy as sa
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
# views
from .views.home import home
from .views.user import user
from .views.index import index
# models
from .models import db
from .models.User import User, Role
from .models.Anime import Anime
# config module
from config import *


def create_app():
    """create and configure the application"""
    anibook = Flask(__name__)

    # configurations file
    anibook.config.from_object('config')

    db.init_app(anibook)

    # flask_mail
    mail = Mail(anibook)
    mail.init_app(anibook)

    # flask_security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    anibook.security = Security(anibook, user_datastore)

    # Blueprints
    anibook.register_blueprint(index)
    anibook.register_blueprint(user, url_prefix='/user')
    anibook.register_blueprint(home)

    # create all tables
    # with anibook.app_context():
    
             

        
    return anibook


def import_csv_data():
    """import csv"""
    df = pd.read_csv('anime.csv')
    
    df['id'] = pd.to_numeric(df['id'], errors='coerce')
    
    df['num_episodes'] = pd.to_numeric(df['num_episodes'], errors='coerce')

    # Convert the 'start_date' column to datetime data type
    df['start_date'] = pd.to_datetime(
        df['start_date'],  format='mixed', dayfirst=True)

    df['end_date'] = pd.to_datetime(
        df['end_date'],  format='mixed', dayfirst=True)

    df['mean'] = pd.to_numeric(df['mean'], errors='coerce')

    df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')

    df['rank'] = pd.to_numeric(df['rank'], errors='coerce')

    df['start_season_year'] = pd.to_numeric(
        df['start_season_year'], errors='coerce')

    df.to_sql('anime', 'postgresql:///anibook',
              if_exists='append', index=False)


def import_csv_data_no_ids():
    """import csv"""
    df = pd.read_csv('anime_no_ids.csv')


    df['num_episodes'] = pd.to_numeric(df['num_episodes'], errors='coerce')

    # Convert the 'start_date' column to datetime data type
    df['start_date'] = pd.to_datetime(
        df['start_date'],  format='mixed', dayfirst=True)

    df['end_date'] = pd.to_datetime(
        df['end_date'],  format='mixed', dayfirst=True)

    df['mean'] = pd.to_numeric(df['mean'], errors='coerce')

    df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')

    df['rank'] = pd.to_numeric(df['rank'], errors='coerce')

    df['start_season_year'] = pd.to_numeric(
        df['start_season_year'], errors='coerce')

    df.to_sql('anime', 'postgresql:///anibook',
              if_exists='append', index=False)


