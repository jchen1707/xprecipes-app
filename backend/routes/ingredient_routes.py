from flask import Blueprint
from backend.app import csrf
from backend.controllers.ingredient_controller import IngredientCreate, IngredientUpdate, \
     IngredientDelete, IngredientList

ingredient_bp = Blueprint('ingredient_bp', __name__)

@ingredient_bp.route('/ingredient', methods=['POST'])
@csrf.exempt
def create_ingredient():
    return IngredientCreate.post()

@ingredient_bp.route('/ingredient/<ingredient_id>', methods=['PUT'])
@csrf.exempt
def update_ingredient(ingredient_id):
    return IngredientUpdate.put(ingredient_id)

@ingredient_bp.route('/ingredient/<ingredient_id>', methods=['DELETE'])\
@csrf.exempt
def delete_ingredient(ingredient_id):
    return IngredientDelete.delete(ingredient_id)

@ingredient_bp.route('/ingredients', methods=['GET'])
def list_ingredients():
    return IngredientList.get()
