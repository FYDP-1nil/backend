from typing import List
from backend.services.mantle.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UserModel(db.Model):
    __tablename__ = "users"

    # id = db.Column(db.Integer, primary_key=True)
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(255), nullable=False, unique=True)
    userpassword = db.Column(db.String(255), nullable=False)
    # access_token = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=False, unique=True)

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id: uuid) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["UserModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
