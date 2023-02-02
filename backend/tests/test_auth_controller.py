import json
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.models import User, Token
from backend.routes import auth_bp
from backend.controllers import auth_controller

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    return app

def test_register_user(client, init_db):
    response = client.post(
        "/register",
        data=json.dumps({"username": "testuser", "password": "testpassword"}),
        headers={"Content-Type": "application/json"},
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert data["message"] == "New user created!"


def test_register_user_duplicate_username(client, init_db):
    response = client.post(
        "/register",
        data=json.dumps({"username": "testuser", "password": "testpassword"}),
        headers={"Content-Type": "application/json"},
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert data["message"] == "Username already exists"


def test_register_user_invalid_payload(client, init_db):
    response = client.post(
        "/register",
        data=json.dumps({"username": "", "password": ""}),
        headers={"Content-Type": "application/json"},
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "username" in data.keys()
    assert "password" in data.keys()


def test_login_user_valid(client, init_db):
    client.post(
        "/register",
        data=json.dumps({"username": "testuser", "password": "testpassword"}),
        headers={"Content-Type": "application/json"},
    )
    response = client.post(
        "/login",
        data=json.dumps({"username": "testuser", "password": "testpassword"}),
        headers={"Content-Type": "application/json"},
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert "access_token" in data.keys()

def test_login_user_invalid(client, init_db):
    response = client.post(
        "/login",
        data=json.dumps({"username": "invaliduser", "password": "invalidpassword"}),
        headers={"Content-Type": "application/json"},
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert data["message"] == "Invalid username or password"

def test_login_user_invalid_payload(client, init_db):
    response = client.post(
        "/login",
        data=json.dumps({"username": "", "password": ""}),
        headers={"Content-Type": "application/json"},
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "username" in data.keys()
    assert "password" in data.keys()


def test_logout_user_valid(client, init_db):
    client.post(
        "/register",
        data=json.dumps({"username": "testuser", "password": "testpassword"}),
        headers={"Content-Type": "application/json"},
    )
    login_response = client.post(
        "/login",
        data=json.dumps({"username": "testuser", "password": "testpassword"}),
        headers={"Content-Type": "application/json"},
    )
    access_token = json.loads(login_response.data.decode())["access_token"]
    response = client.post(
        "/logout", headers={"Authorization": f"Bearer {access_token}"}
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data["message"] == "Successfully logged out"

def test_logout_user_invalid(client, init_db):
    response = client.post("/logout", headers={"Authorization": "Bearer invalidtoken"})
    data = json.loads(response.data.decode())
    assert response.status_code == 401
    assert data["message"] == "Token is invalid"


def test_token_refresh_valid(client, init_db):
    client.post(
        "/register",
        data=json.dumps({"username": "testuser", "password": "testpassword"}),
        headers={"Content-Type": "application/json"},
    )
    login_response = client.post(
        "/login",
        data=json.dumps({"username": "testuser", "password": "testpassword"}),
        headers={"Content-Type": "application/json"},
    )
    refresh_token = json.loads(login_response.data.decode())["refresh_token"]
    response = client.post(
        "/refresh", headers={"Authorization": f"Bearer {refresh_token}"}
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert "access_token" in data.keys()

def test_token_refresh_invalid(client, init_db):
    response = client.post("/refresh", headers={"Authorization": "Bearer invalidtoken"})
    data = json.loads(response.data.decode())
    assert response.status_code == 401
    assert data["message"] == "Token is invalid"
