
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
