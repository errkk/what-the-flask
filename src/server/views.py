from flask import Blueprint, jsonify

from server.models import User
from server.schemas import UserSchema

# Create an instance of the User schema, to convert User model instances into dictionaries, which
# can be serialised into JSON
user_schema = UserSchema()

# Make a namespace for all the views defined in here.
# This will be added to flask at the setups stage so it can route requests to these functions
views = Blueprint("views", __name__)

# This is the main route that you get when you go to http://localhost:5000/
@views.route("/")
def index():
    # Some data to return
    data = {"ha": "ai"}

    # Return a JSON response
    return jsonify(data)


@views.route("/user/<user_id>")
def user(user_id):
    # Get a single object
    user = User.query.get(user_id)

    if user is None:
        return jsonify({"status": "not found"}), 404

    # User objects are complex python objects, and they don't know how to be serialised by JSON
    # Marshmallow schemas are used to convert model instances into dictionaries, which can be
    # encoded as json, and returned to the client as an API response
    serializable_data = user_schema.dump(user)

    # Return a JSON response
    return jsonify(serializable_data)


@views.route("/users")
def users():
    # Get a collection of objects
    users = User.query.all()

    # User objects are complex python objects, and they don't know how to be serialised by JSON
    # Marshmallow schemas are used to convert model instances into dictionaries, which can be
    # encoded as json, and returned to the client as an API response
    serializable_data = user_schema.dump(users, many=True)

    # Return a JSON response
    return jsonify(serializable_data)
