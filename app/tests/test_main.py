from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

data = {
  "email": "user@example.com",
  "phone": 3113346355,
  "first_name": "string",
  "last_name": "string",
  "password": "string"
}

def test_api_funciona():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == { "mensaje" : "Bienvenido"}


def test_get_all_users():
    response = client.get("/usuarios")
    assert response.status_code ==200


def test_create_user():
    response = client.post("/usuarios/", json=data)
    assert response.status_code == 200
    body = response.json()
    assert body.get("email") == "user@example.com"
    assert body.get("phone") == 3113346355
    assert body.get("first_name") == "string"
    assert body.get("last_name") == "string"


    # asegurarnos de que no regrese la contraseña cuando se crea un usuario
    assert "password" not in body.keys()

def test_create_user_fail():
    response = client.post("/usuarios/", json=data)
    assert response.status_code == 409


def test_get_specific_user():
    response = client.get(f"/usuarios/user@example.com")
    assert response.status_code == 200

def test_delete_specific_user():
    response = client.delete(f"/usuarios/user@example.com")
    assert response.status_code == 200