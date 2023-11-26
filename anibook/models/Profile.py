"""User model"""
from datetime import datetime
from flask_security.models import fsqla_v3 as fsqla
from . import db


role_profile = db.Table(
    "profile_role",
    db.Column("profile_id", db.Integer(), db.ForeignKey("profile.id")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
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
    profile_image = db.Column(db.String(), default="../static/images/profile_image.png")
    active = db.Column(db.Boolean, default=True)
    roles = db.relationship(
        "Role", secondary="profile_role", backref=db.backref("profile", lazy="dynamic")
    )

    watching_id = db.Column(db.Integer(), db.ForeignKey("watching.id"))
    completed_id = db.Column(db.Integer(), db.ForeignKey("completed.id"))
    backlogged_id = db.Column(db.Integer(), db.ForeignKey("backlogged.id"))

    watching = db.relationship("Watching")
    completed = db.relationship("Completed")
    backlogged = db.relationship("Backlogged")

    def __repr__(self):
        return f"Profile('{self.username}', '{self.email}')"


class Watching(db.Model):
    """Watching model"""

    __tablename__ = "watching"
    id = db.Column(db.Integer(), primary_key=True)
    anime_id = db.Column(db.Integer(), db.ForeignKey("anime.id"))
    anime = db.relationship("Anime")


class Completed(db.Model):
    """Completed model"""

    __tablename__ = "completed"
    id = db.Column(db.Integer(), primary_key=True)
    anime_id = db.Column(db.Integer(), db.ForeignKey("anime.id"))
    anime = db.relationship("Anime")


class Backlogged(db.Model):
    """Backlogged model"""

    __tablename__ = "backlogged"
    id = db.Column(db.Integer(), primary_key=True)
    anime_id = db.Column(db.Integer(), db.ForeignKey("anime.id"))
    anime = db.relationship("Anime")


# flask-security


class Role(db.Model, fsqla.FsRoleMixin):
    __tablename__ = "role"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))
