from flask import Blueprint
from backend.app import csrf
from backend.controllers.ingredient_controller import IngredientCreate, IngredientUpdate, \
     IngredientDelete, IngredientList

ingredient_bp = Blueprint("ingredient_bp", __name__)

IngredientCreate_instance = IngredientCreate()
IngredientUpdate_instance = IngredientUpdate()
IngredientDelete_instance = IngredientDelete()
IngredientGet_instance = IngredientList()

@ingredient_bp.route("/ingredient", methods=["POST"])
def create_ingredient():
    return IngredientCreate_instance.post()

@ingredient_bp.route("/ingredient/<ingredient_id>", methods=["PUT"])
def update_ingredient(ingredient_id):
    return IngredientUpdate_instance.put(ingredient_id)

@ingredient_bp.route("/ingredient/<ingredient_id>", methods=["DELETE"])
def delete_ingredient(ingredient_id):
    return IngredientDelete_instance.delete(ingredient_id)

@ingredient_bp.route("/ingredients", methods=["GET"])
def list_ingredients():
    return IngredientGet_instance.get()
