import pytest
import json
from flask import Flask
from backend.controllers import cook_controller
from backend.models import Recipe, IngredientStorage
from backend import db
from backend.routes import cook_bp
from backend.config import SQL_ALCHEMY_DATABASE_URI, SECRET_KEY
from app import create_app

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(cook_bp)
    return app

def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = SQL_ALCHEMY_DATABASE_URI
    app.config["SECRET_KEY"] = SECRET_KEY
    client = app.test_client()
    yield client


def test_cook_recipe_with_valid_id(client):
    data = {
        "title": "test recipe",
        "ingredients": "test ingredients",
        "ingredient_quantity": 1,
        "unit": "g",
        "calories": 100,
        "cooktime": 20
    }
    response = client.post("/recipe", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 201
    recipe = json.loads(response.data)
    recipe_id = recipe["id"]

    ingredient = recipe["ingredients"]
    ingredient_quantity = recipe["ingredient_quantity"]
    data = {
        "ingredient": ingredient,
        "amount": ingredient_quantity + 1
    }
    response = client.post("/storage", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 201

    response = client.post(f"/cook/{recipe_id}")
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data["message"] == "Recipe cooked successfully."

    storage = IngredientStorage.query.filter_by(ingredient=ingredient).first()
    assert storage.amount == 1

def test_cook_recipe_with_invalid_id(client):
    response = client.post("/cook/1000")
    assert response.status_code == 404
    response_data = json.loads(response.data)
    assert response_data["error"] == "Recipe not found."

def test_cook_recipe_with_insufficient_ingredients(client):
    recipe_data = {
        "title": "test recipe",
        "ingredients": "test ingredients",
        "ingredient_quantity": 5,
        "unit": "g",
        "calories": 100,
        "cooktime": 20
    }
    response = client.post("/recipe", data=json.dumps(recipe_data), content_type="application/json")
    recipe_id = json.loads(response.data)['id']

    ingredient_data = {
        "ingredient": "test ingredients",
        "amount": 2,
        "unit": "g"
    }
    client.post("/ingredient", data=json.dumps(ingredient_data), content_type="application/json")

    response = client.post(f"/cook/{recipe_id}")
    assert response.status_code == 400
    error = json.loads(response.data)
    assert error["error"] == "Ingredient not available or insufficient amount."

def test_cook_recipe_with_non_existent_recipe(client):
    response = client.post("/cook/1")
    assert response.status_code == 404
    error = json.loads(response.data)
    assert error["error"] == "Recipe not found."
