from flask import request,jsonify
from flask_restful import Resource
from backend.models import Recipe 
from S3_helpers import get_image_url 

class RecipeCreate(Resource):
    def post(self):
        title = request.json['title']
        ingredients = request.json['ingredients']
        ingredient_quantity = request.json['ingredient_quantity']
        unit = request.json['unit']
        image_key = request.json['image_key']
        calories = request.json['calories']
        cooktime = request.json['cooktime']
        recipe = Recipe(title=title,ingredients=ingredients,ingredient_quantity=ingredient_quantity
                        ,unit=unit,image_key=image_key,calories=calories,cooktime=cooktime)
        recipe.save()
        recipe.image_url = get_image_url(recipe.image_key,"xprecipes-images")
        recipe.save()
        return recipe.to_dict(), 201

class RecipeUpdate(Resource):
    def put(self,recipe_id):
        title = request.json['title']
        ingredients = request.json['ingredients']
        ingredient_quantity = request.json['ingredient_quantity']
        unit = request.json['unit']
        image_key = request.json['image_key']
        calories = request.json['calories']
        cooktime = request.json['cooktime']
        recipe = Recipe.query.filter_by(id=recipe_id).first()
        recipe.title = title
        recipe.ingredients = ingredients
        recipe.quantity = ingredient_quantity
        recipe.unit = unit
        recipe.image_key = image_key
        recipe.calories = calories
        recipe.cooktime = cooktime 
        recipe.save()
        recipe.image_url = get_image_url(recipe,image_key,'xprecipes_images')
        return recipe.to_dict(), 200

class RecipeDelete(Resource):
    def delete(self,recipe_id):
        recipe = Recipe.query.filter_by(id=recipe_id).first()
        recipe.delete()
        return {'message': 'Recipe deleted'}, 200

class RecipeList(Resource):
    def get(self):
        recipes = Recipe.query.all()
        return [recipe.to_dict() for recipe in recipes]      
