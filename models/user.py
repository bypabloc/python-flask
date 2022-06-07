from models.base import BaseModel
from models.base import db


class User(BaseModel):
    """
    User model
    """
    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(length=255),
        nullable=False,
        unique=True,
    )
    email = db.Column(
        db.String(length=255),
        nullable=False,
        unique=True,
    )
    password = db.Column(
        db.String(length=255),
        nullable=False,
        unique=True,
    )

    created_at = db.Column(
        db.DateTime,
        default=db.func.now(),
    )
    updated_at = db.Column(
        db.DateTime,
        default=None,
    )
    deleted_at = db.Column(
        db.DateTime,
        default=None,
    )

    def save(self, *args, **kwargs):
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()
        return user

    def save_bulk(self, list: list = None):
        if list is None:
            return False
        users = []
        for item in list:
            user = User(**item)
            db.session.add(user)
            users.append(user)
        db.session.commit()
        return users

    def delete(self):
        db.session.delete(self)
        db.session.commit()
