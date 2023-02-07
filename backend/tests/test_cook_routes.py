import json
import pytest
from backend import create_app
from backend.models import IngredientStorage

@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_cook_recipe_with_invalid_id(client):
    response = client.post("/cook/0")
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
    assert response.status_code == 201
    recipe = json.loads(response.data)
    recipe_id = recipe["id"]

    response = client.post(f"/cook/{recipe_id}")
    assert response.status_code == 400
    response_data = json.loads(response.data)
    assert response_data["error"] == "Ingredient not available or insufficient amount."

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
