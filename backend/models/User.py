from backend.controllers import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    tokens = db.relationship('Token', backref='user', lazy=True)
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
