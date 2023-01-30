import json
import pytest
from backend.config import SQL_ALCHEMY_DATABASE_URI, SECRET_KEY
from backend.models import Recipe
from app import create_app

@pytest.fixture
def app():
    return create_app()

def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = SQL_ALCHEMY_DATABASE_URI
    app.config["SECRET_KEY"] = SECRET_KEY
    client = app.test_client()
    yield client

def test_create_recipe(client):
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
    assert recipe["title"] == "test recipe"
    assert recipe["ingredients"] == "test ingredients"
    assert recipe["ingredient_quantity"] == 1
    assert recipe["unit"] == "g"
    assert recipe["calories"] == 100
    assert recipe["cooktime"] == 20

def test_update_recipe(client):
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
    update_data = {
        "title": "updated test recipe",
        "ingredients": "updated test ingredients",
        "ingredient_quantity": 2,
        "unit": "oz",
        "calories": 200,
        "cooktime": 30
    }
    response = client.put("/recipe/{}".format(recipe["id"]), data=json.dumps(update_data), content_type="application/json")
    assert response.status_code == 200
    recipe = json.loads(response.data)
    assert recipe["title"] == "updated test recipe"
    assert recipe["ingredients"] == "updated test ingredients"
    assert recipe["ingredient_quantity"] == 2
    assert recipe["unit"] == "oz"
    assert recipe["calories"] == 200
    assert recipe["cooktime"] == 30

    
def test_get_recipe(client):
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
    response = client.get("/recipe/{}".format(recipe["id"]))
    assert response.status_code == 200
    recipe = json.loads(response.data)
    assert recipe["title"] == "test recipe"
    assert recipe["ingredients"] == "test ingredients"
    assert recipe["ingredient_quantity"] == 1
    assert recipe["unit"] == "g"
    assert recipe["calories"] == 100
    assert recipe["cooktime"] == 20

def test_delete_recipe(client):
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
    response = client.delete("/recipe/{}".format(recipe["id"]))
    assert response.status_code == 204
    response = client.get("/recipe/{}".format(recipe["id"]))
    assert response.status_code == 404
