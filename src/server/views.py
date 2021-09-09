from flask import Blueprint, jsonify

from server.models import User

# Make a namespace for all the views defined in here.
# This will be added to flask at the setups stage so it can route requests to these functions
views = Blueprint('views', __name__)

# This is the main route that you get when you go to http://localhost:5000/
@views.route('/')
def index():
    # Some data to return
    data = {"ha": "ai"}

    # Return a JSON response
    return jsonify(data)


@views.route('/users')
def users():
    # Some data to return
    data = {"ha": "ai"}
    users = User.query.all()

    # Return a JSON response
    return jsonify([u.name for u in users])
