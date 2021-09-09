from flask import Flask

from server.views import views
from server.database import db

# Set up Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

# Tell Flask about all the routes in the views module
app.register_blueprint(views)

# Tell Flask about our database
db.init_app(app)


# If this file is run like `python server/app.py` then the program starts
# This is what docker does when we start it up
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')