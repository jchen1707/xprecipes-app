from flask import Blueprint, jsonify
from backend.controllers import cook_controller

cook_bp = Blueprint("cook_bp", __name__)

controller = cook_controller()

@cook_bp.route("/cook/<recipe_id>", methods=["POST"])
def cook_recipe(recipe_id):
    response = controller.cook_recipe(recipe_id)
    return jsonify(response), response["status_code"]
