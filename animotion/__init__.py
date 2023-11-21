"""app module"""
import os
from flask import Flask
from flask_security import hash_password, Security, SQLAlchemyUserDatastore
from flask_mail import Mail
#views
from .views.home import home
from .views.user import user
from .views.index import index
#models
from .models import db
from .models.user_profile import UserProfile, Role
#forms
from .forms.CustomLoginForm import CustomLoginForm
from .forms.CustomRegisterForm import CustomRegisterForm

def create_app():
    """create and configure the app"""
    animotion = Flask(__name__)

    #set configurations for the application
    animotion.config['SECRET_KEY'] = "z8-oCrPLq7H8R2N5U-soOkzfamJ39qylYft02gMdwgU"
    
    # Initialize the shared database (the same SQLAchemy instace is shared across all the models)
    animotion.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///animotion'
    animotion.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # setup Flask-Security
    animotion.config['SECURITY_PASSWORD_SALT'] = "281789554452959811915070470802888875921"
    # have session and remember cookie be samesite (flask/flask_login)
    animotion.config['REMEMBER_COOKIE_SAMESITE'] = "strict"
    animotion.config['SESSION_COOKIE_SAMESITE'] = "strict"
    # This option makes sure that DB connections from the
    # pool are still valid. Important for entire application since
    # many DBaaS options automatically close idle connections.
    animotion.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True, }
    animotion.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'security/custom_login.html'
    
    db.init_app(animotion)

    
   
    animotion.config['SECURITY_REGISTER_USER_TEMPLATE'] = 'security/custom_register.html'
    animotion.config['SECURITY_CONFIRMABLE'] = False
    animotion.config['SECURITY_EMAIL_SUBJECT_REGISTER'] = "(◕‿◕) Welcome to Animotion!"
    animotion.config['SECURITY_POST_REGISTER_VIEW'] ="/home"
    animotion.config['SECURITY_DEFAULT_REMEMBER_ME'] = True
    animotion.config['SECURITY_POST_LOGIN_VIEW'] = "/home"
    animotion.config['SECURITY_LOGIN_FORM'] = CustomLoginForm
    animotion.config['SECURITY_REGISTER_FORM'] = CustomRegisterForm
    
    #flask-mail config
    animotion.config['MAIL_SERVER'] = "smtp.gmail.com"
    animotion.config['MAIL_PORT'] = 587
    animotion.config['MAIL_USE_TLS'] = True
    animotion.config['MAIL_USERNAME'] = "theanimotionteam@gmail.com"
    animotion.config['MAIL_PASSWORD'] = "xvqvdfzgmvuituhl"
    
    mail = Mail(animotion)
    
    animotion.config['SECURITY_REGISTERABLE'] = True
    animotion.config['SECURITY_USERNAME_ENABLE'] = True
    animotion.config['SECURITY_USERNAME_REQUIRED'] = True
    animotion.config['SECURITY_REGISTER_URL'] = "/signup"
    animotion.config['SECURITY_RECOVERABLE'] = True
    animotion.config['SECURITY_RESET_PASSWORD_TEMPLATE'] = "security/custom_reset.html"
    animotion.config['SECURITY_FORGOT_PASSWORD_TEMPLATE'] = "security/custom_forgot.html"
    
    
    
    user_datastore = SQLAlchemyUserDatastore(db, UserProfile, Role)
    animotion.security = Security(animotion, user_datastore)

    # Register view Blueprints
    animotion.register_blueprint(index)
    animotion.register_blueprint(user, url_prefix='/user')
    animotion.register_blueprint(home)
    
    

    #create all the db tables
    with animotion.app_context():
        db.create_all()

    return animotion



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
   
