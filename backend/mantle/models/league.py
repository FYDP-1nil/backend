from typing import List
from backend.mantle.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class LeagueModel(db.Model):
    __tablename__ = "leagues"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    league_name = db.Column(db.String(255), nullable=False, unique=True)
    league_password = db.Column(db.String(255), nullable=False)

    @classmethod
    def find_by_league_name(cls, league_name: str) -> "LeagueModel":
        return cls.query.filter_by(league_name=league_name).first()

    @classmethod
    def find_by_id(cls, _id: uuid) -> "LeagueModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["LeagueModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
