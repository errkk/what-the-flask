
def test_index(client, add_user):
    """ Test that a user can be retrived by ID
    """
    user = add_user()

    response = client.get(f"/user/{user.id}")
    assert response.json["email"] == user.email
    assert response.json["name"] == user.name
    assert response.status_code == 200
