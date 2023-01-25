from flask import request
from flask_restful import Resource
from cerberus import Validator
from backend.models import IngredientStorage

class IngredientCreate(Resource):
    def post(self):
        data = request.get_json()
        v = Validator(validation_schema)
        if not v.validate(data):
            return v.errors, 400
        title = request.json['title']
        ingredients = request.json['ingredients']
        quantity = request.json['quantity']
        unit = request.json['unit']
        recipe = IngredientStorage(title=title,ingredients=ingredients,quantity=quantity,unit=unit)
        recipe.save()
        return recipe.to_dict(), 201

class IngredientUpdate(Resource):
    def put(self,recipe_id):
        data = request.get_json()
        v = Validator(validation_schema)
        if not v.validate(data):
            return v.errors, 400
        title = request.json['title']
        ingredients = request.json['ingredients']
        quantity = request.json['quantity']
        unit = request.json['unit']
        recipe = IngredientStorage.query.filter_by(id=recipe_id).first()
        recipe.title = title
        recipe.ingredients = ingredients
        recipe.quantity = quantity
        recipe.unit = unit
        recipe.save()
        return recipe.to_dict(), 200

class IngredientDelete(Resource):
    def delete(self,recipe_id):
        recipe = IngredientStorage.query.filter_by(id=recipe_id).first()
        recipe.delete()
        return {'message': 'Recipe deleted'}, 200

class IngredientList(Resource):
    def get(self):
        recipes = IngredientStorage.query.all()
        return [recipe.to_dict() for recipe in recipes]      

validation_schema = {
    "name": {
        "type": "string",
        "required": True
    },
    "quantity": {
        "type": "float",
        "required": True
    },
    "unit": {
        "type": "string",
        "required": True,
        "allowed": ["oz", "g", "cup", "tsp", "tbsp", "ml", "l"]
    }
}


