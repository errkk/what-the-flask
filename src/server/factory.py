import os

from flask import Flask
from flask_migrate import Migrate

from server.views import views


def create_app(settings_override=None):
    # Set up Flask
    app = Flask(__name__)
    # Config set here. It could be a file if we woudld add more things
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]

    # Override config for test
    if settings_override is not None:
        app.config.update(settings_override)

    from server.database import db, ma

    # Tell Flask about all the routes in the views module
    app.register_blueprint(views)

    # Tell Flask about our database
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    return app
