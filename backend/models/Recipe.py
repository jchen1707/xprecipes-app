from backend import db
from backend.S3_helpers import get_image_url

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    ingredient_quantity = db.Column(db.Float(), nullable=False)
    unit = db.Column(db.String(255), nullable=False)
    image_key = db.Column(db.String(255), nullable=True)
    calories = db.Column(db.Integer, nullable=False)
    cooktime = db.Column(db.Interval, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


    def __init__(self, title, ingredients, instructions, ingredient_quantity, unit,
             calories, cooktime, image_key = None):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.ingredient_quantity = ingredient_quantity
        self.unit = unit
        self.image_key = image_key
        self.calories = calories 
        self.cooketime = cooktime

    def to_dict(self):
        recipe_data = {
            "id": self.id,
            "title": self.title,
            "ingredients": self.ingredients,
            "quantity": self.ingredient_quantity,
            "unit": self.unit,
            "image_key": self.image_key,
            "calories": self.calories,
            "cooktime": self.cooktime,
        }
        if self.image_key:
            recipe_data["image_url"] = get_image_url(self.image_key, "xprecipes-images")
        return recipe_data