from backend import db

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    expires = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, token, user_id, expires):
        self.token = token
        self.user_id = user_id
        self.expires = expires
