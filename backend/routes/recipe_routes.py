from flask import Blueprint,jsonify
from backend.controllers import recipe_controller
from backend import csrf_validation_middleware

recipe_bp = Blueprint("recipe_bp", __name__)

controller = recipe_controller()

@recipe_bp.before_request
def csrf_validation():
    csrf_validation_middleware()

@recipe_bp.route("/recipe", methods=["POST"])
def create_recipe():
    response = controller.create_recipe()
    return jsonify(response), response["status_code"]

@recipe_bp.route("/recipe/<recipe_id>", methods=["PUT"])
def update_recipe(recipe_id):
    response = controller.update_recipe(recipe_id)
    return jsonify(response), response["status_code"]

@recipe_bp.route("/recipe/<recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    response = controller.delete_recipe(recipe_id)
    return jsonify(response), response["status_code"]

@recipe_bp.route("/recipes", methods=["GET"])
def list_recipes():
    response = controller.list_recipes()
    return jsonify(response), response["status_code"]
