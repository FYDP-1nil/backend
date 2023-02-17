from backend.services.mantle.ma import ma
from backend.services.mantle.models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_only = ("userpassword",)
        dump_only = ("id",)
        load_instance = True
