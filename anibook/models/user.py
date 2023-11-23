"""SQLAlchemy model for user_profile table."""
from datetime import datetime
from flask_security.models import fsqla_v3 as fsqla
from . import db


roles_users = db.Table('roles_users', db.Column('user_id', db.Integer, db.      ForeignKey(
    'users.id')), db.Column('role_id', db.Integer, db.ForeignKey('roles.id')))


class User(db.Model, fsqla.FsUserMixin):
    """user profile model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), nullable=False, unique=True)

    username = db.Column(db.String(30), nullable=False, unique=True,)

    password = db.Column(db.String(128), nullable=False)

    profile_image = db.Column(
        db.String(), default="../static/images/profile_image.png")

    active = db.Column(db.Boolean, default = True)

    confirmed_at = db.Column(db.DateTime(), default=datetime.utcnow)
    
    roles = db.relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('user', lazy='dynamic')
    )

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))


def init_app(app):
    """anitialize this database"""
    db.init_app(app)

   