from typing import List
from backend.mantle.db import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

class GameModel(db.Model):
    __tablename__ = "game"

    id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), primary_key=True, default=uuid.uuid4)
    team_1 = db.Column(db.String(255), nullable=False, unique=True)
    team_2 = db.Column(db.String(255), nullable=False, unique=True)
    stream_created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    stream_ended_at = db.Column(db.DateTime(timezone=True), default=func.now())
    game_started_at = db.Column(db.DateTime(timezone=True), default=func.now())
    game_ended_at = db.Column(db.DateTime(timezone=True), default=func.now())
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


    # @classmethod
    #def find_by_league_name(cls, league_name: str) -> "GameModel":
    #    return cls.query.filter_by(league_name=league_name).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "GameModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["GameModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
