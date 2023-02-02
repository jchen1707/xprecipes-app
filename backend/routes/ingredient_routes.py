from flask import Blueprint, jsonify,request
from backend.controllers.ingredient_controller import IngredientController
from backend import csrf_validation_middleware

ingredient_bp = Blueprint("ingredient_bp", __name__)

controller = IngredientController()

@ingredient_bp.before_request
def csrf_validation():
    csrf_validation_middleware()

@ingredient_bp.route("/ingredient", methods=["POST"])
def create_ingredient():
    response = controller.create_ingredient()
    return jsonify(response), response["status_code"]

@ingredient_bp.route("/ingredient/<ingredient_id>", methods=["PUT"])
def update_ingredient(ingredient_id):
    response = controller.update_ingredient(ingredient_id)
    return jsonify(response), response["status_code"]

@ingredient_bp.route("/ingredient/<ingredient_id>", methods=["DELETE"])
def delete_ingredient(ingredient_id):
    response = controller.delete_ingredient(ingredient_id)
    return jsonify(response), response["status_code"]

@ingredient_bp.route("/ingredients", methods=["GET"])
def list_ingredients():
    user_id = request.headers.get("user_id")
    response = controller.list_ingredients(user_id)
    return jsonify(response), response["status_code"]

