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

@pytest.fixture
def client(app):
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = SQL_ALCHEMY_DATABASE_URI
    app.config["SECRET_KEY"] = SECRET_KEY
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_cook_recipe_with_valid_id(client):
    recipe_data = {
        "title": "test recipe",
        "ingredients": "test ingredients",
        "ingredient_quantity": 1,
        "unit": "g",
        "calories": 100,
        "cooktime": 20
    }
    response = client.post("/recipe", data=json.dumps(recipe_data), content_type="application/json")
    assert response.status_code == 201
    recipe = json.loads(response.data)
    recipe_id = recipe["id"]

    ingredient_data = {
        "ingredient": recipe["ingredients"],
        "amount": recipe["ingredient_quantity"] + 1,
        "unit": recipe["unit"]
    }
    response = client.post("/storage", data=json.dumps(ingredient_data), content_type="application/json")
    assert response.status_code == 201

    response = client.post(f"/cook/{recipe_id}")
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data["message"] == "Recipe cooked successfully."

    storage = IngredientStorage.query.filter_by(ingredient=ingredient_data["ingredient"]).first()
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

    # Add the recipe
    response = client.post("/recipe/", json=recipe_data)
    assert response.status_code == 201

    # Try to cook the recipe with insufficient ingredients
    response = client.post("/cook/", json={"recipe_id": 1, "ingredient_quantity": 4})
    assert response.status_code == 400
    assert response.json() == {"message": "Insufficient ingredients to cook the recipe"}
