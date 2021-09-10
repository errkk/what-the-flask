import os

from flask import Flask
from flask_migrate import Migrate

from server.views import views
from server.database import db, ma


# Set up Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

# Tell Flask about all the routes in the views module
app.register_blueprint(views)

# Tell Flask about our database
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)
