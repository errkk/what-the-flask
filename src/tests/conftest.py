import os

import pytest
from flask_migrate import Migrate, upgrade
from sqlalchemy_utils.functions import drop_database, create_database, database_exists

from server.models import User
from server.factory import create_app
from server.database import db as _db


TEST_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"] + "_test"

@pytest.fixture(scope="session")
def app(request):
    """Session-wide test `Flask` application."""
    settings_override = {"SQLALCHEMY_DATABASE_URI": TEST_DATABASE_URI}

    if database_exists(TEST_DATABASE_URI):
        drop_database(TEST_DATABASE_URI)

    create_database(TEST_DATABASE_URI)
    app = create_app(settings_override)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="session", autouse=True)
def db(app, request):
    """Session-wide test database."""

    _db.app = app

    # Apply migrations to the database
    Migrate(app, _db)
    upgrade()

    return _db


@pytest.fixture(scope="function")
def add_user(db):
    def inner(name="Test user", email="test@example.com"):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    return inner

