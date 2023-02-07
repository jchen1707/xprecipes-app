from backend import db
from backend.models import Recipe
from backend.models import IngredientStorage

UNIT_CONVERSIONS = {
    "oz": {"g": 28.3495, "cup": 1.0, "tsp": 6.0, "tbsp": 2.0, "ml": 29.5735, "l": 0.0295735},
    "g": {"oz": 0.035274, "cup": 0.00446429, "tsp": 0.202884, "tbsp": 0.067628, "ml": 1.0, "l": 0.001},
    "cup": {"oz": 1.0, "g": 236.588, "tsp": 48.0, "tbsp": 16.0, "ml": 236.588, "l": 0.236588},
    "tsp": {"oz": 0.166667, "g": 4.92892, "cup": 0.0208333, "tbsp": 0.333333, "ml": 4.92892, "l": 0.00492892},
    "tbsp": {"oz": 0.5, "g": 14.7868, "cup": 0.0625, "tsp": 3.0, "ml": 14.7868, "l": 0.0147868},
    "ml": {"oz": 0.033814, "g": 1.0, "cup": 0.00422675, "tsp": 0.202884, "tbsp": 0.067628, "l": 0.001},
    "l": {"oz": 33.814, "g": 1000.0, "cup": 4.22675, "tsp": 202.884, "tbsp": 67.628, "ml": 1000.0}
}


def cook_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return {"error": "Recipe not found."}, 404
    ingredient = recipe.ingredients
    ingredient_quantity = recipe.ingredient_quantity
    unit = recipe.unit
    storage = IngredientStorage.query.filter_by(ingredient=ingredient).first()
    if not storage:
        return {"error": "Ingredient not available."}, 400
    if unit != storage.unit:
        try:
            ingredient_quantity = convert_units(ingredient_quantity, unit, storage.unit)
        except Exception as e:
            return {"error": str(e)}, 400
    if storage.amount < ingredient_quantity:
        return {"error": "Insufficient amount."}, 400
    storage.amount -= ingredient_quantity
    db.session.commit()
    return {"message": "Recipe cooked successfully."}, 200

def convert_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = UNIT_CONVERSIONS[from_unit]
    if to_unit not in conversions:
        return None
    return value * conversions[to_unit]