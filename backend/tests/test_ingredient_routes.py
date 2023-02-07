import pytest
import json
from flask import Flask
from backend.routes import ingredient_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(ingredient_bp)
    return app

def test_create_ingredient(client):
    response = client.post('/ingredient')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_update_ingredient(client):
    response = client.put('/ingredient/1')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_delete_ingredient(client):
    response = client.delete('/ingredient/1')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_list_ingredients(client):
    response = client.get('/ingredients')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)
