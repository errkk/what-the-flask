from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Setup SQL Alchemy. We import db around the place to interact with the database
db = SQLAlchemy()
ma = Marshmallow()
