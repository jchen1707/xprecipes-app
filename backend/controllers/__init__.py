from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from backend.routes.recipe_routes import recipe_bp
from backend.routes.auth_routes import auth_bp
from backend.routes.ingredient_routes import ingredient_bp
from backend.config import SQL_ALCHEMY_DATABASE_URI, SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQL_ALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


app.register_blueprint(recipe_bp)
app.register_blueprint(ingredient_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8000)