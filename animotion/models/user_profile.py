"""SQLAlchemy model for user_profile table."""
from datetime import datetime
from flask_security.models import fsqla_v3 as fsqla
from . import db


roles_user_profile = db.Table('roles_users', db.Column('user_id', db.Integer, db.      ForeignKey(
    'user_profile.id')), db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class UserProfile(db.Model, fsqla.FsUserMixin):
    """user profile model"""

    __tablename__ = "user_profile"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), nullable=False, unique=True)

    username = db.Column(db.String(30), nullable=False, unique=True,)

    password = db.Column(db.String(128), nullable=False)

    profile_image = db.Column(
        db.String(), default="../static/images/profile_image.png")

    date_of_birth = db.Column(db.Date, nullable=False)

    active = db.Column(db.Boolean)

    confirmed_at = db.Column(db.DateTime(), default=datetime.utcnow)
    
    roles = db.relationship(
        'Role',
        secondary=roles_user_profile,
        backref=db.backref('user_profiles', lazy='dynamic')
    )

    def __repr__(self):
        return f"UserProfile('{self.username}', '{self.email}')"



class Role(db.Model, fsqla.FsRoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))


def init_app(app):
    """anitialize this database"""
    db.init_app(app)

   
