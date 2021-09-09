from server.database import db
from server.models import User, Role

if __name__ == "__main__":
    from server.app import app

    with app.app_context():

        print("Inserting some test data")
        r = Role(name="can do stuff")
        r2 = Role(name="can do loads of stuff")
        u = User(name="Lesley", email="test@example.com", roles=[r, r2])
        u2 = User(name="Bob", email="testbob@example.com", roles=[r])
        db.session.add(u)
        db.session.add(u2)
        db.session.commit()
