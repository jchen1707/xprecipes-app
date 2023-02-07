import pytest
import json
from flask import Flask
from backend import db
from backend.models import IngredientStorage
from app import create_app
from backend import db
from backend.routes import ingredient_bp
from backend.config import SQL_ALCHEMY_DATABASE_URI, SECRET_KEY

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(ingredient_bp)
    return app

def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = SQL_ALCHEMY_DATABASE_URI
    app.config["SECRET_KEY"] = SECRET_KEY
    yield client
    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_create_ingredient(client):
    data = {
    "ingredient": "sugar",
    "amount": 100,
    "unit": "g"
    }
    response = client.post("/api/ingredient", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 201
    assert response.json["ingredient"] == "sugar"
    assert response.json["amount"] == 100
    assert response.json["unit"] == "g"

def test_create_ingredient_missing_required_field(client):
    data = {
        "amount": 100,
        "unit": "g"
    }
    response = client.post("/api/ingredient", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 400
    assert response.json["message"] == "Bad request: 'ingredient' is a required field"

def test_create_ingredient_incorrect_data_type(client):
    data = {
        "ingredient": 100,
        "amount": 100,
        "unit": "g"
    }
    response = client.post("/api/ingredient", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 400
    assert response.json["message"] == "Bad request: Incorrect data type for field 'ingredient'"


def test_update_ingredient(client):
    ingredient = IngredientStorage(ingredient="sugar", amount=100, unit="g")
    db.session.add(ingredient)
    db.session.commit()
    data = {
        "ingredient": "salt",
        "amount": 50,
        "unit": "g"
    }
    response = client.put(f"/api/ingredient/{ingredient.id}", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 200
    assert response.json["ingredient"] == "salt"
    assert response.json["amount"] == 50
    assert response.json["unit"] == "g"

def test_update_ingredient_incorrect_data_type(client):
    ingredient = IngredientStorage(ingredient="sugar", amount=100, unit="g")
    db.session.add(ingredient)
    db.session.commit()

    data = {
        "ingredient": 100,
        "amount": 50,
        "unit": "g"
    }
    response = client.put(f"/api/ingredient/{ingredient.id}", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 400
    assert response.json["message"] == "Bad request: Incorrect data type for field 'ingredient'"

def test_delete_ingredient(client):
    ingredient = IngredientStorage(ingredient="sugar", amount=100, unit="g")
    db.session.add(ingredient)
    db.session.commit()
    response = client.delete(f"/api/ingredient/{ingredient.id}")
    assert response.status_code == 200
    assert response.json["message"] == "Ingredient deleted"

def test_delete_ingredient_invalid_id(client):
    response = client.delete("/api/ingredient/0")
    assert response.status_code == 404
    assert response.json["message"] == "Not found: Ingredient not found"

def test_get_ingredient(client):
    ingredient = IngredientStorage(ingredient="sugar", amount=100, unit="g")
    db.session.add(ingredient)
    db.session.commit()
    response = client.get(f"/api/ingredient/{ingredient.id}")
    assert response.status_code == 200
    assert response.json["ingredient"]

def test_get_ingredient_invalid_id(client):
    response = client.get("/api/ingredient/0")
    assert response.status_code == 404
    assert response.json["message"] == "Not found: Ingredient not found"