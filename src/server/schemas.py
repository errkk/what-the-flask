from marshmallow import fields

from server.database import ma
from server.models import User

# Schemas are used to help Models and other datastructures to be serialised into JSON
# They're quite like how modles map object properties to table columns, except this time
# they map object properties to JSON keys
# They can also be used to process JSON data coming in, and create model instances from the data

class UserSchema(ma.SQLAlchemySchema):
    # These are the fields that we want to be in the JSON output
    # The auto_field function tells it to look at the model, to find out what data type
    # to expect, eg, integer, string, list etc.
    name = ma.auto_field()
    email = ma.auto_field()

    # This is a schema that works with an SQLA model
    # So we tell it here, which type of model to expect
    class Meta:
        model = User
