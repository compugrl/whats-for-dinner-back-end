from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from dotenv import load_dotenv
from app.models.recipe import Recipe
from ..helpers.helper_functions import validate_recipe, parse_recipe

load_dotenv()

recipe_bp = Blueprint("recipe_bp", __name__, url_prefix="/recipes")

@recipe_bp.route("", methods=["GET"])
# Not used in code but needed for testing purposes
def get_all_recipes():
    recipes_response = []
    recipes = Recipe.query.all()
    recipes_response = [recipe.to_dict() for recipe in recipes]

    return jsonify(recipes_response)

@recipe_bp.route("/<recipe_id>", methods=["GET"])
def get_one_recipe(recipe_id):
    recipe = validate_recipe(recipe_id)
    
    return {"recipe": recipe.to_dict()}

@recipe_bp.route("", methods=["POST"])
def create_recipe():    
    request_body = request.get_json()  
    new_recipe = Recipe.create(request_body)
    
    db.session.add(new_recipe)
    db.session.commit()

    return make_response(jsonify({"recipe": new_recipe.to_dict()}), 201) 

@recipe_bp.route("/<recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = validate_recipe(recipe_id)

    db.session.delete(recipe)
    db.session.commit()
    
    return jsonify({'success': f'Recipe {recipe.label} successfully deleted'})

@recipe_bp.route("/<recipe_id>", methods=["PATCH"])
def edit_recipe(recipe_id):
    recipe = validate_recipe(recipe_id) 
    request_body = request.get_json()

    if "hash" in request_body:
        recipe.hash = request_body["hash"]        
    if "label" in request_body:
        recipe.label = request_body["label"]
    if "image_tnail" in request_body:
        recipe.image_tnail = request_body["image_tnail"] 
    if "image_sm" in request_body:
        recipe.image_sm = request_body["image_sm"]   
    db.session.commit()

    return {"updated recipe": recipe.to_dict()}