"""app module"""
import os
from flask import Flask
from flask_security import hash_password, Security, SQLAlchemyUserDatastore
#views
from .views.home import home
from .views.user import user
from .views.index import index
#models
from .models import db
from .models.user_profile import UserProfile, Role
#forms
from .forms.CustomLoginForm import CustomLoginForm


def create_app():
    """create and configure the app"""
    animotion = Flask(__name__)

    #set configurations for the application
    animotion.config['SECRET_KEY'] = "z8-oCrPLq7H8R2N5U-soOkzfamJ39qylYft02gMdwgU"
    
    # Initialize the shared database (the same SQLAchemy instace is shared across all the models)
    animotion.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///animotion'
    animotion.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(animotion)

    # setup Flask-Security
    animotion.config['SECURITY_PASSWORD_SALT'] = "281789554452959811915070470802888875921"
    # have session and remember cookie be samesite (flask/flask_login)
    animotion.config['REMEMBER_COOKIE_SAMESITE'] = "strict"
    animotion.config['SESSION_COOKIE_SAMESITE'] = "strict"
    # This option makes sure that DB connections from the
    # pool are still valid. Important for entire application since
    # many DBaaS options automatically close idle connections.
    animotion.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True, }
    animotion.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'security/custom-login.html'
    animotion.config['SECURITY_POST_LOGIN_VIEW'] = "/home"
    animotion.config['SECURITY_LOGIN_FORM'] = CustomLoginForm
    animotion.config['SECURITY_REGISTERABLE'] = True
    
    user_datastore = SQLAlchemyUserDatastore(db, UserProfile, Role)
    animotion.security = Security(animotion, user_datastore)

    # Register view Blueprints
    animotion.register_blueprint(index)
    animotion.register_blueprint(user, url_prefix='/user')
    animotion.register_blueprint(home)
    
    

    # Seed data
    seed_data(animotion)

    return animotion


def seed_data(app):
    """seed dummy data for testing"""
    
    # one time setup
    with app.app_context():
        # Create user_profiles to start/test with
        db.drop_all()
        db.create_all()
        if not app.security.datastore.find_user(email="test@me.com"):
            app.security.datastore.create_user(
                email="test@me.com", username="testsecurity", date_of_birth="1998-12-12", password=hash_password("password"))
            app.security.datastore.create_user(
                email="test2@me.com", username="testsecurity2", date_of_birth="1998-12-12", password=hash_password("loco"))
            
        db.session.commit()
   
