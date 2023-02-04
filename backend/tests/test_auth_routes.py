import json
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.models import User, Token
from backend.controllers import auth_controller
from backend.routes import auth_bp


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    return app


def test_register(client, app):
    response = client.post("/auth/register",
                           data=json.dumps({
                               "username": "testuser",
                               "password": "testpassword"
                           }),
                           headers={
                               "Content-Type": "application/json"
                           })
    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert "message" in data.keys()
    assert data["message"] == "User created successfully."

def test_register_invalid(client,app):
    response = client.post("/auth/register",
                           data=json.dumps({
                               "username": "",
                               "password": ""
                           }),
                           headers={
                               "Content-Type": "application/json"
                           })
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "message" in data.keys()
    assert data["message"] == "Username and password are required."

def test_login_valid(client, app):
    client.post("/auth/register",
                data=json.dumps({
                    "username": "testuser",
                    "password": "testpassword"
                }),
                headers={
                    "Content-Type": "application/json"
                })
    response = client.post("/auth/login",
                           data=json.dumps({
                               "username": "testuser",
                               "password": "testpassword"
                           }),
                           headers={
                               "Content-Type": "application/json"
                           })
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert "access_token" in data.keys()

def test_login_invalid(client,app):
    response = client.post("/auth/login",
                           data=json.dumps({
                               "username": "invaliduser",
                               "password": "invalidpassword"
                           }),
                           headers={
                               "Content-Type": "application/json"
                           })
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert data["message"] == "Invalid username or password"


def test_logout_valid(client):
    client.post("/auth/register",
                data=json.dumps({
                    "username": "testuser",
                    "password": "testpassword"
                }),
                headers={
                    "Content-Type": "application/json"
                })
    login_response = client.post("/auth/login",
                                 data=json.dumps({
                                     "username": "testuser",
                                     "password": "testpassword"
                                 }),
                                 headers={
                                     "Content-Type": "application/json"
                                 })
    login_data = json.loads(login_response.data.decode())
    access_token = login_data["access_token"]

    response = client.post("/auth/logout",
                           headers={
                               "Authorization": f"Bearer {access_token}"
                           })
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data["message"] == "Successfully logged out"

def test_logout_missing_token(client):
    response = client.post("/auth/logout")
    data = json.loads(response.data.decode())
    assert response.status_code == 401
    assert data["message"] == "Missing access token"

def test_logout_invalid_token(client):
    response = client.post("/auth/logout",
                           headers={
                               "Authorization": "Bearer invalidtoken"
                           })
    data = json.loads(response.data.decode())
    assert response.status_code == 401
    assert data["message"] == "Invalid access token"