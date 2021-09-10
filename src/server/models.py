from server.database import db

# Models are Python classes that describe database tables, each model is a different table
# These are used for 3 things

# - Migrations
#   When we want to add a field to a model, it is added here, and we specify what type of data
#   it will be. e.g. Integer, String, etc.
#   Then we can use the migration tool to make a new DB version file (in migrations/versions)
#   which can be used to upgrade the database to the new version, adding all the correct tables
#   columns etc to the database.

# - Queries
#   The db.Model class comes with a method called query, which allows us to query that table
#   The ORM will convert the python code into an SQL query, that will be sent to the database
#   For example to list all users the query `User.query.all()` would make the SQL:
#   `SELECT * FROM user`


# - Inserting data
#   The model instances can also be saved to the database as a new row. To do this, the model
#   class is instantiated and added to the db transaction. When committed the data will be saved.
#   The model can also be validated, to ensure that the data is in the right format
#   Eg to make a new user
#   `user = User(name="Gladys", email="glad@aol.com")`
#   And it is saved by
#   `db.session.add(user)`
#   `db.session.commit()`

# - Validating data
#   Certain rules for what some fields can be can be enforced by models. So a model can be
#   created with some fields, and checked to see if they are suitable for our business logic.


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
