from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from dotenv import load_dotenv
from app.models.recipe import Recipe
from app.models.user import User
from ..helpers.helper_functions import validate_recipe, validate_user
from sqlalchemy import and_

load_dotenv()

recipe_bp = Blueprint("recipe_bp", __name__, url_prefix="/recipes")

@recipe_bp.route("", methods=["GET"])
# Not used in code but needed for testing purposes
def get_all_recipes():
    recipes_response = []
    recipes = Recipe.query.all()
    recipes_response = [recipe.to_dict() for recipe in recipes]

    return jsonify(recipes_response)

@recipe_bp.route("/<rhash>", methods=["GET"])
def get_one_recipe(rhash):
    recipe = Recipe.query.get(rhash)
    if recipe:
        return {"recipe": recipe.to_dict()}
    else:
        return make_response(jsonify(f"Recipe {rhash} not found"), 404)

@recipe_bp.route("", methods=["POST"])
def create_recipe():
    request_body = request.get_json()
    new_recipe = Recipe.create(request_body)

    db.session.add(new_recipe)
    db.session.commit()

    return make_response(jsonify({"recipe": new_recipe.to_dict()}), 201)

@recipe_bp.route("/<rhash>", methods=["DELETE"])
def delete_recipe(rhash):
    recipe = validate_recipe(rhash)

    db.session.delete(recipe)
    db.session.commit()

    return jsonify({'success': f'Recipe {recipe.label} successfully deleted'})