import bleach
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from cerberus import Validator
from backend import db
from backend.models import IngredientStorage

validation_schema = {
    "ingredient": {
        "type": "string",
        "required": True
    },
    "amount": {
        "type": "float",
        "required": True
    },
    "unit": {
        "type": "string",
        "required": True,
        "allowed": ["oz", "g", "cup", "tsp", "tbsp", "ml", "l"]
    }
}

class IngredientCreate(Resource):
    @jwt_required
    def post(self): 
        data = request.json
        v = Validator(validation_schema)
        if not v.validate(data):
            return v.errors, 400
        ingredient = bleach.clean(data["ingredient"])
        amount = data["amount"]
        unit = bleach.clean(data["unit"])
        existing_ingredient = IngredientStorage.query.filter_by(ingredient=ingredient).first()
        if existing_ingredient:
            return {"message": "Ingredient already exists"}, 400
        ingredient_storage = IngredientStorage(ingredient=ingredient,amount=amount,unit=unit)
        db.session.add(ingredient_storage)
        db.session.commit()
        return ingredient_storage.to_dict(), 201

class IngredientUpdate(Resource):
    @jwt_required
    def put(self, ingredient_id):
        data = request.get_json()
        v = Validator(validation_schema)
        if not v.validate(data):
            return v.errors, 400
        ingredient_storage = IngredientStorage.query.get(ingredient_id)
        if ingredient_storage is None:
            return {"message": "Ingredient not found"}, 404
        ingredient = bleach.clean(data["ingredient"])
        amount = data["amount"]
        unit = bleach.clean(data["unit"])
        ingredient_storage.ingredient = ingredient
        ingredient_storage.amount = amount
        ingredient_storage.unit = unit
        db.session.commit()
        return ingredient_storage.to_dict(), 200    

class IngredientDelete(Resource):
    @jwt_required
    def delete(self, ingredient_id):
        ingredient_storage = IngredientStorage.query.get(ingredient_id)
        if ingredient_storage is None:
            return {"message": "Ingredient not found"}, 404
        db.session.delete(ingredient_storage)
        db.session.commit()
        return {"message": "Ingredient deleted"}, 200


class IngredientList(Resource):
    @jwt_required
    def get(self, ingredient_id):
        user_id = get_jwt_identity()
        ingredients = IngredientStorage.query.filter_by(id=ingredient_id, user_id=user_id).first()
        if ingredients is None:
            return {"message": "Ingredient not found"}, 404
        return ingredients.to_dict()

