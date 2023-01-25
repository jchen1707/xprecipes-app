from flask import Blueprint
from backend.controllers.recipe_controller import RecipeCreate, RecipeUpdate, RecipeDelete, RecipeList

recipe_bp = Blueprint('recipe_bp', __name__)

@recipe_bp.route('/recipe', methods=['POST'])
def create_recipe():
    return RecipeCreate.post()

@recipe_bp.route('/recipe/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    return RecipeUpdate.put(recipe_id)

@recipe_bp.route('/recipe/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    return RecipeDelete.delete(recipe_id)

@recipe_bp.route('/recipes', methods=['GET'])
def list_recipes():
    return RecipeList.get()
