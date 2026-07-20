def test_login_success(client):
    response = client.post("/login", data={"user":"juan","password":"123"})
    assert response.status_code == 200
    assert b"Bienvenido" in response.data
