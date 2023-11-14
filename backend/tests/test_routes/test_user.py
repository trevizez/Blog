def test_create_user(client):
    data = {"email": "testuser@mail.ru", "password": "testing"}
    response = client.post("/", json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "testuser@mail.ru"
    assert response.json()["is_active"] == True
