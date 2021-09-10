from marshmallow import fields

from server.database import ma
from server.models import User


class UserSchema(ma.SQLAlchemySchema):
    name = ma.auto_field()

    class Meta:
        model = User
