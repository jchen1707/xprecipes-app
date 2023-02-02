from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from backend.routes import recipe_bp, auth_bp, ingredient_bp,cook_bp
from backend.config import SQL_ALCHEMY_DATABASE_URI, SECRET_KEY

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQL_ALCHEMY_DATABASE_URI
    app.config["SECRET_KEY"] = SECRET_KEY
    db.init_app(app)

    @app.teardown_appcontext
    def close_db(error):
        try:
            db.session.remove()
        except Exception as e:
             app.logger.error("Error while closing database: %s", str(e))
             
    app.register_blueprint(recipe_bp)
    app.register_blueprint(ingredient_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cook_bp)

    return app
