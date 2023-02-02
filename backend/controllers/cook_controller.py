from backend import db
from backend.models import Recipe
from backend.models import IngredientStorage

def cook_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return {"error": "Recipe not found."}, 404
    ingredient = recipe.ingredients
    ingredient_quantity = recipe.ingredient_quantity
    storage = IngredientStorage.query.filter_by(ingredient=ingredient).first()
    if not storage or storage.amount < ingredient_quantity:
        return {"error": "Ingredient not available or insufficient amount."}, 400
    storage.amount -= ingredient_quantity
    db.session.commit()
    return {"message": "Recipe cooked successfully."}, 200
