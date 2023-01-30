from flask import Blueprint, request
from backend.app import db
from backend.models import IngredientStorage

cook_bp = Blueprint("cook_bp", __name__)

@cook_bp.route("/cook", methods=["POST"])
def cook_recipe():
    ingredient_name = request.json['ingredient_name']
    amount = request.json['amount']

    ingredient = IngredientStorage.query.filter_by(name=ingredient_name).first()
    if ingredient is None:
        return "Ingredient does not exist", 400
    if ingredient.amount < amount:
        return "Not enough ingredient in storage", 400
    ingredient.amount -= amount
    db.session.commit()
    return "Success", 200
