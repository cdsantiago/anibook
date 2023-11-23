"""app module"""
import os
import datetime
from pandas import pandas as pd
from flask import Flask
from flask_security import hash_password, Security, SQLAlchemyUserDatastore
from flask_mail import Mail
# views
from .views.home import home
from .views.user import user
from .views.index import index
# models
from .models import db
from .models.user import User, Role
from .models.anime import Anime
# forms
from .forms.CustomLoginForm import CustomLoginForm
from .forms.CustomRegisterForm import CustomRegisterForm


def create_app():
    """create and configure the app"""
    anibook = Flask(__name__)

    # set configurations for the application
    anibook.config['SECRET_KEY'] = "z8-oCrPLq7H8R2N5U-soOkzfamJ39qylYft02gMdwgU"

    # Initialize the shared database (the same SQLAchemy instace is shared across all the models)
    anibook.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///anibook'
    anibook.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # setup Flask-Security
    anibook.config['SECURITY_PASSWORD_SALT'] = "281789554452959811915070470802888875921"
    # have session and remember cookie be samesite (flask/flask_login)
    anibook.config['REMEMBER_COOKIE_SAMESITE'] = "strict"
    anibook.config['SESSION_COOKIE_SAMESITE'] = "strict"
    # This option makes sure that DB connections from the
    # pool are still valid. Important for entire application since
    # many DBaaS options automatically close idle connections.
    anibook.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True, }
    anibook.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'security/custom_login.html'

    db.init_app(anibook)

    anibook.config['SECURITY_REGISTER_USER_TEMPLATE'] = 'security/custom_register.html'
    anibook.config['SECURITY_CONFIRMABLE'] = False
    anibook.config['SECURITY_EMAIL_SUBJECT_REGISTER'] = "Welcome to Anibook!"
    anibook.config['SECURITY_POST_REGISTER_VIEW'] = "/home"
    anibook.config['SECURITY_DEFAULT_REMEMBER_ME'] = True
    anibook.config['SECURITY_POST_LOGIN_VIEW'] = "/home"
    anibook.config['SECURITY_LOGIN_FORM'] = CustomLoginForm
    anibook.config['SECURITY_REGISTER_FORM'] = CustomRegisterForm

    # flask-mail config
    anibook.config['MAIL_SERVER'] = "smtp.gmail.com"
    anibook.config['MAIL_PORT'] = 587
    anibook.config['MAIL_USE_TLS'] = True
    anibook.config['MAIL_USERNAME'] = "theanimotionteam@gmail.com"
    anibook.config['MAIL_PASSWORD'] = "xvqvdfzgmvuituhl"

    mail = Mail(anibook)

    anibook.config['SECURITY_REGISTERABLE'] = True
    anibook.config['SECURITY_USERNAME_ENABLE'] = True
    anibook.config['SECURITY_USERNAME_REQUIRED'] = True
    anibook.config['SECURITY_REGISTER_URL'] = "/signup"
    anibook.config['SECURITY_RECOVERABLE'] = True
    anibook.config['SECURITY_RESET_PASSWORD_TEMPLATE'] = "security/custom_reset.html"
    anibook.config['SECURITY_FORGOT_PASSWORD_TEMPLATE'] = "security/custom_forgot.html"

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    anibook.security = Security(anibook, user_datastore)

    # Register view Blueprints
    anibook.register_blueprint(index)
    anibook.register_blueprint(user, url_prefix='/user')
    anibook.register_blueprint(home)

    df = pd.read_csv('anime.csv')
    
    df['num_episodes'] = pd.to_numeric(df['num_episodes'], errors='coerce')
    
    # Convert the 'start_date' column to datetime data type
    df['start_date'] = pd.to_datetime(df['start_date'],  format='mixed', dayfirst=True)
  
    df['end_date'] = pd.to_datetime(df['end_date'],  format='mixed', dayfirst=True)
    
    df['mean'] = pd.to_numeric(df['mean'], errors='coerce')
    
    df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
    
    df['rank'] = pd.to_numeric(df['rank'], errors='coerce')
    
    df['start_season_year'] = pd.to_numeric(df['start_season_year'], errors='coerce')
    
    df.to_sql('anime', 'postgresql:///anibook',
              if_exists='append', index=False)
    

    # create all the db tables
    with anibook.app_context():
        db.create_all()

    return anibook


# seed test data function
# def seed_data(app):
#     """seed dummy data for testing"""

#     # one time setup
#     with app.app_context():
#         # Create user_profiles to start/test with
#         db.drop_all()
#         db.create_all()
#         if not app.security.datastore.find_user(email="test@me.com"):
#             app.security.datastore.create_user(
#                 email="test@me.com", username="testsecurity", password=hash_password("password"))
#             app.security.datastore.create_user(
#                 email="test2@me.com", username="testsecurity2", password=hash_password("loco"))

#         db.session.commit()
