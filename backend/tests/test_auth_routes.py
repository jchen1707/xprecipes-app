import pytest
import json
from flask import Flask
from backend.routes import auth_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    return app

def test_register(client):
    response = client.post('/auth/register', data=json.dumps({"username": "test_user", "password": "test_password"}), content_type='application/json')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_login(client):
    response = client.post('/auth/login', data=json.dumps({"username": "test_user", "password": "test_password"}), content_type='application/json')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_logout(client):
    response = client.post('/auth/logout')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)
import pytest
import json
from flask import Flask
from backend.routes import auth_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    return app

def test_register(client):
    response = client.post('/auth/register', data=json.dumps({"username": "test_user", "password": "test_password"}), content_type='application/json')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_login(client):
    response = client.post('/auth/login', data=json.dumps({"username": "test_user", "password": "test_password"}), content_type='application/json')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_logout(client):
    response = client.post('/auth/logout')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)
