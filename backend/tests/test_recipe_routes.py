import pytest
import json
from flask import Flask
from backend.routes import recipe_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(recipe_bp)
    return app

def test_create_recipe(client):
    response = client.post('/recipe')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_update_recipe(client):
    response = client.put('/recipe/1')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_delete_recipe(client):
    response = client.delete('/recipe/1')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)

def test_list_recipes(client):
    response = client.get('/recipes')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)
