from backend import db

class IngredientStorage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float(), nullable=False)
    unit = db.Column(db.String(255), nullable=False)
    
    def __init__(self, ingredient, amount, unit):
        self.ingredient = ingredient
        self.amount = amount
        self.unit = unit
        
    def to_dict(self):
        return {
            "id": self.id,
            "ingredient": self.ingredient,
            "amount": self.amount,
            "unit": self.unit,
        }
