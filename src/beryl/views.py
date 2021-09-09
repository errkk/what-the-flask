from flask import Blueprint, jsonify

views = Blueprint('views', __name__)

@views.route('/')
def index():
    data = {"ha": "ai"}
    return jsonify(data)

