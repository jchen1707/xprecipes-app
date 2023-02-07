import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend import db
from backend.models import Recipe, IngredientStorage
from backend.controllers import cook_controller
from backend.routes import cook_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_cook_recipe_success(client):
    recipe = Recipe(
        title="Test Recipe",
        ingredients="Test Ingredient",
        ingredient_quantity=1,
        unit="Unit",
        calories=100,
        cooktime=10,
        image_key="test_image_key"
    )
    db.session.add(recipe)
    db.session.commit()
    storage = IngredientStorage(
        ingredient="Test Ingredient",
        amount=2
    )
    db.session.add(storage)
    db.session.commit()

    response = client.post(f"/cook/{recipe.id}")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Recipe cooked successfully."}

def test_cook_recipe_not_found(client):
    response = client.post("/cook/1")
    assert response.status_code == 404
    assert response.get_json() == {"error": "Recipe not found."}

def test_cook_recipe_ingredient_not_available(client):
    recipe = Recipe(
        title="Test Recipe",
        ingredients="Test Ingredient",
        ingredient_quantity=1,
        unit="Unit",
        calories=100,
        cooktime=10,
        image_key="test_image_key"
    )
    db.session.add(recipe)
    db.session.commit()

    response = client.post(f"/cook/{recipe.id}")
    assert response.status_code == 400
    assert response.get_json() == {"error": "Ingredient not available or insufficient amount."}
