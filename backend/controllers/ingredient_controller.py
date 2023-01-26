import bleach
from flask import request
from flask_restful import Resource
from flask_wtf.csrf import validate_csrf
from flask_jwt_extended import jwt_required
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
        if not validate_csrf(request.form.get("csrf_token")):
            return {"message": "Invalid CSRF token"}, 400        
        data = request.get_json()
        v = Validator(validation_schema)
        if not v.validate(data):
            return v.errors, 400
        ingredient = bleach.clean(data["ingredient"])
        amount = data["amount"]
        unit = bleach.clean(data["unit"])
        ingredient_storage = IngredientStorage(ingredient=ingredient,amount=amount,unit=unit)
        db.session.add(ingredient_storage)
        db.session.commit()
        return ingredient_storage.to_dict(), 201

class IngredientUpdate(Resource):
    @jwt_required
    def put(self, ingredient_id):
        if not validate_csrf(request.form.get("csrf_token")):
            return {"message": "Invalid CSRF token"}, 400        
        data = request.get_json()
        v = Validator(validation_schema)
        if not v.validate(data):
            return v.errors, 400
        ingredient = bleach.clean(request.json["ingredient"])
        amount = request.json["quantity"]
        unit = bleach.clean(request.json["unit"])
        ingredient_storage = IngredientStorage.query.filter_by(id=ingredient_id).first()
        if ingredient_storage is None:
            return {"message": "Ingredient not found"}, 404
        ingredient_storage.ingredient = ingredient
        ingredient.amount = amount
        ingredient_storage.unit = unit
        ingredient_storage.save()
        return ingredient_storage.to_dict(), 200

class IngredientDelete(Resource):
    @jwt_required
    def delete(self,ingredient_id):
        if not validate_csrf(request.form.get("csrf_token")):
            return {"message": "Invalid CSRF token"}, 400 
        Ingredient = IngredientStorage.query.filter_by(id=ingredient_id).first()
        Ingredient.delete()
        return {"message": "Ingredient deleted"}, 200

class IngredientList(Resource):
    @jwt_required
    def get(self):
        if not validate_csrf(request.form.get("csrf_token")):
            return {"message": "Invalid CSRF token"}, 400 
        ingredient_storage = IngredientStorage.query.all()
        return [ingredient_storage.to_dict() for Ingredient in IngredientStorage]
  

