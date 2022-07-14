from backend.mantle.ma import ma
from backend.mantle.models.league import LeagueModel


class LeagueSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LeagueModel
        # load_only = ("password", "access_token",)
        # load_only = ("password",)
        # dump_only = ("id",)
        load_instance = True
