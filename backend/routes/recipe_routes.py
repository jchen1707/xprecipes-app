from flask import Blueprint
from backend.controllers.recipe_controller import RecipeCreate, RecipeUpdate, RecipeDelete, RecipeList

recipe_bp = Blueprint("recipe_bp", __name__)

RecipeCreate_instance = RecipeCreate()
RecipeUpdate_instance = RecipeUpdate()
RecipeDelte_instance = RecipeDelete()
RecipeGet_instance = RecipeList()

@recipe_bp.route("/recipe", methods=["POST"])
def create_recipe():
    return RecipeCreate_instance.post()

@recipe_bp.route("/recipe/<recipe_id>", methods=["PUT"])
def update_recipe(recipe_id):
    return RecipeUpdate_instance.put(recipe_id)

@recipe_bp.route("/recipe/<recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    return RecipeDelte_instance.delete(recipe_id)

@recipe_bp.route("/recipes", methods=["GET"])
def list_recipes():
    return RecipeGet_instance.get()
