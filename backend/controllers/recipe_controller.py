from flask import request
from flask_restful import Resource
from backend.models import Recipe 
from backend.S3_helpers import get_image_url,upload_to_s3 
from backend.controllers import app

class RecipeCreate(Resource):
    def post(self):
        title = request.json['title']
        ingredients = request.json['ingredients']
        ingredient_quantity = request.json['ingredient_quantity']
        unit = request.json['unit']
        image = request.files['image']
        image_url = upload_to_s3(app, image, "xprecipes-images")
        image_key = image_url.split("/")[-1]
        calories = request.json['calories']
        cooktime = request.json['cooktime']
        recipe = Recipe(title=title,ingredients=ingredients,ingredient_quantity=ingredient_quantity
                        ,unit=unit,image_key=image_key,calories=calories,cooktime=cooktime)
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
        recipe.image_url = get_image_url(recipe,image_key,'xprecipes_images')
        recipe.save()
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
