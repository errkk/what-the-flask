from server.database import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.Text, nullable=False)

    # User belongs to a category, so we store the category_id in a column
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    # This tells SQLA that the user has a relationship to category
    # So someone looking at category.users would see whos in there as well as user.category
    category = db.relationship('Category', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.title

# Just like in app.py if this file is run like `python server/models.py` then the stuff below runs
# We dont want this to happen when this file is imported, just when we want to run it
# We'll use this for runing the database migrations
if __name__ == '__main__':
    from server.app import app

    with app.app_context():
        db.create_all()

        c = Category()
        c.name = "some people"

        u = User()
        u.name = "Lesley"
        u.email = "test@example.com"
        u.category = c

        db.session.add_all([c, u])
        db.session.commit()
