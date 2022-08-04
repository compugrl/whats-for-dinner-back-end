from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    from app.models.recipe import Recipe
    from app.models.user import User
    from app.models.user_recipe import UserRecipe
    from app.models.shopping_list import Shopping_list

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.edamam import edamam_bp
    from .routes.user import user_bp
    from .routes.recipe import recipe_bp
    from .routes.user_recipe import ur_bp
    from .routes.shopping_list import shopping_list_bp

    app.register_blueprint(edamam_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(recipe_bp)
    app.register_blueprint(ur_bp)
    app.register_blueprint(shopping_list_bp)

    return app
