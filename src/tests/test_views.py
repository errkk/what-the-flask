from server.models import User


def test_index(client, add_user):
    """ Test that a user can be retrived by ID
    """
    # Create a user in the test database
    # so that there will be one in the response
    user = add_user()

    # Use the test client to hit the endpoint we're testing
    # It retuns a response object that we can make assertions on
    response = client.get(f"/user/{user.id}")
    
    # Checking attributes of the response to see if they
    # match the expected values
    assert response.json["email"] == user.email
    assert response.json["name"] == user.name

    # A successful HTTP request has a code of 200
    assert response.status_code == 200
    
    response = client.get("/user/123")

    assert response.status_code == 404

def test_insert_user(client):

    users = User.query.count()

    assert users == 0

    invalid_user_data = {"name": "Suzie"}
    response = client.post("/users", json=invalid_user_data)

    users = User.query.count()
    assert users == 0
    assert response.status_code == 422

    user_data = {
        "name": "Suzie",
        "email": "Suzie@suzie.com"
        }
    response = client.post("/users", json=user_data)

    users = User.query.count()
    assert users == 1
    assert response.status_code == 201

