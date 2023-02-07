import pytest
import json
from flask import Flask
from backend.routes import cook_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(cook_bp)
    return app

def test_cook_recipe(client):
    response = client.post('/cook/1')
    assert response.status_code == 200
    assert 'status_code' in json.loads(response.data)
