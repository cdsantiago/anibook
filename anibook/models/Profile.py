"""User model"""
from datetime import datetime
from flask_security.models import fsqla_v3 as fsqla
from . import db


# association table, necessary for many to many relationships
role_profile = db.Table(
    "profile_role",
    db.Column("profile_id", db.Integer(), db.ForeignKey("profile.id")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
)
completed_anime = db.Table(
    'completed_anime',
    db.Column('completed_id', db.Integer, db.ForeignKey('completed.id')),
    db.Column('anime_id', db.Integer, db.ForeignKey('anime.id'))
)

watching_anime = db.Table(
    'watching_anime',
    db.Column('watching_id', db.Integer, db.ForeignKey('watching.id')),
    db.Column('anime_id', db.Integer, db.ForeignKey('anime.id'))
)

backlogged_anime = db.Table(
    'backlogged_anime',
    db.Column('backlogged_id', db.Integer, db.ForeignKey('backlogged.id')),
    db.Column('anime_id', db.Integer, db.ForeignKey('anime.id'))
)


class Profile(db.Model, fsqla.FsUserMixin):
    """Profile/user model"""

    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(
        db.String(30),
        nullable=False,
        unique=True,
    )
    password = db.Column(db.String(128), nullable=False)
    profile_image = db.Column(
        db.String(), default="../static/images/profile_image.png")
    active = db.Column(db.Boolean, default=True)
    roles = db.relationship(
        "Role", secondary="profile_role", backref=db.backref("profile", lazy="dynamic")
    )

    completed = db.relationship(
        "Completed",
        backref="profile",
        cascade="all, delete-orphan"
    )

    watching = db.relationship(
        "Watching",
        backref="profile",
        cascade="all, delete-orphan"
    )

    backlogged = db.relationship(
        "Backlogged",
        backref="profile",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Profile('{self.username}', '{self.email}')"


class Completed(db.Model):
    """Completed model"""

    __tablename__ = "completed"
    id = db.Column(db.Integer(), primary_key=True)
    anime = db.relationship(
        "Anime",
        secondary=completed_anime,
        backref="completed"
    )
    profile_id = db.Column(
        db.Integer,
        db.ForeignKey("profile.id")
    )


class Watching(db.Model):
    """Watching model"""

    __tablename__ = "watching"
    id = db.Column(db.Integer(), primary_key=True)
    anime = db.relationship(
        "Anime",
        secondary=watching_anime,
        backref="watching"
    )
    profile_id = db.Column(
        db.Integer(),
        db.ForeignKey("profile.id")
    )


class Backlogged(db.Model):
    """Backlogged model"""

    __tablename__ = "backlogged"
    id = db.Column(db.Integer(), primary_key=True)
    anime = db.relationship(
        "Anime",
        secondary=backlogged_anime,
        backref="backlogged"
    )
    profile_id = db.Column(
        db.Integer(),
        db.ForeignKey("profile.id")
    )


# flask-security


class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = "role"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))
