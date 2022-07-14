from backend.mantle.ma import ma
from backend.mantle.models.game import GameModel


class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GameModel
        # load_only = ("password", "access_token",)
        # load_only = ("password",)
        # dump_only = ("id",)
        load_instance = True
