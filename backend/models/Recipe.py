from backend import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.String(255), nullable=True)
    unit = db.Column(db.String(255), nullable=True)

    def __init__(self, title, ingredients, instructions, quantity=None, unit=None):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.quantity = quantity
        self.unit = unit

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'ingredients': self.ingredients,
            'quantity': self.quantity,
            'unit': self.unit,
        }