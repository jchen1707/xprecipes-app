import json
import pytest
from flask import Flask
from backend.config import SQL_ALCHEMY_DATABASE_URI, SECRET_KEY
from backend.routes import auth_bp
from app import create_app
from backend import db

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
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

def test_create_recipe_with_required_fields(client):
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

def test_create_recipe_with_missing_required_field(client):
    data = {
        "ingredients": "test ingredients",
        "ingredient_quantity": 1,
        "unit": "g",
        "calories": 100,
        "cooktime": 20
    }
    response = client.post("/recipe", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 400

def test_create_recipe_with_incorrect_data_type(client):
    data = {
        "title": "test recipe",
        "ingredients": "test ingredients",
        "ingredient_quantity": "one",
        "unit": "g",
        "calories": 100,
        "cooktime": 20
    }
    response = client.post("/recipe", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 400


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
    response = client.put(f"/recipe/{recipe['id']}", data=json.dumps(update_data), content_type="application/json")
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

def test_get_recipe_with_invalid_id(client):
    response = client.get("/recipe/999")
    assert response.status_code == 404


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
