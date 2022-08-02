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

@recipe_bp.route("/<id>", methods=["GET"])
def get_one_recipe(id):
    recipe = validate_recipe(id)
    
    return {"recipe": recipe.to_dict()}

@recipe_bp.route("", methods=["POST"])
def create_recipe():    
    request_body = request.get_json()  
    new_recipe = Recipe.create(request_body)
    
    db.session.add(new_recipe)
    db.session.commit()

    return make_response(jsonify({"recipe": new_recipe.to_dict()}), 201) 

@recipe_bp.route("/<id>/users/<user_id>", methods=["DELETE"])
def delete_recipe(id, user_id):
    recipe = validate_recipe(id)
    user = validate_user(user_id)

    db.session.delete(recipe)
    db.session.commit()
    
    return jsonify({'success': f'Recipe {recipe.label} successfully deleted'})

@recipe_bp.route("/<id>", methods=["PATCH"])
def edit_recipe(id):
    recipe = validate_recipe(id) 
    request_body = request.get_json()

    if "hash" in request_body:
        recipe.hash = request_body["hash"]        
    if "label" in request_body:
        recipe.label = request_body["label"]
    if "image_url" in request_body:
        recipe.image_tnail = request_body["image_url"] 
    if "shareAs" in request_body:
        recipe.image_sm = request_body["shareAs"]   
    db.session.commit()

    return {"updated recipe": recipe.to_dict()}

@recipe_bp.route("/users/<user_id>", methods=["GET"])
def get_recipes_per_user(user_id):
    user = validate_user(user_id)
    params = False
    date_param = request.args.get("menu_date")
    fave_param = request.args.get("favorite")

    if date_param:     
        params = True
        recipes_info = [recipe.to_dict() for recipe in user.recipe if recipe.menu_date == date_param]        

    if fave_param:     
        params = True
        recipes_info = [recipe.to_dict() for recipe in user.recipe if recipe.favorite == True]          


    if not params:
        recipes_info = [recipe.to_dict() for recipe in user.recipe]     
    
    db.session.commit()

    return make_response(jsonify(recipes_info)), 200