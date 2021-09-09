from server.database import db


class User(db.Model):
    __table_name__ = "users"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.Text, nullable=False)

    roles = db.relationship("models.Role", backref="roles", lazy=True, cascade="all,delete")

    def __repr__(self):
        return f"<User:{self.id} {self.name}>"


class Role(db.Model):
    __table_name__ = "categorys"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)


    def __repr__(self):
        return f"<Category:{self.id} {self.name}>"


# Just like in app.py if this file is run like `python server/models.py` then the stuff below runs
# We dont want this to happen when this file is imported, just when we want to run it
# We'll use this for runing the database migrations
if __name__ == "__main__":
    from server.app import app

    with app.app_context():
        db.drop_all()
        db.create_all()
