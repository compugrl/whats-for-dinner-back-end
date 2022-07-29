from flask import Blueprint, request, jsonify, make_response
from app import db
from dotenv import load_dotenv
from app.models.user import User
from .recipe import create_recipe
from ..helpers.helper_functions import validate_user, validate_recipe

load_dotenv()

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

@user_bp.route("", methods=["GET"])
def get_all_users():
    users = User.query
    users = users.all()

    users_response = []
    for user in users:
        users_response.append(user.to_dict())
    
    return jsonify(users_response)

@user_bp.route("/<user_id>", methods=["GET"])
def get_one_user(user_id):
    user = validate_user(user_id)
    
    return {"user": user.to_dict()}

@user_bp.route("", methods=["POST"])
def create_user():
    request_body = request.get_json()
    if "name" not in request_body:
        return make_response(jsonify(dict("User must have a name")), 400)
    if "email" not in request_body:
        return make_response(jsonify(dict("User must have a valid email address")), 400)
    if "days_to_display" not in request_body:
        return make_response(jsonify(dict("User must have days to display")), 400)
    
    new_user = User.create(request_body)
    
    db.session.add(new_user)
    db.session.commit()

    return make_response(jsonify({"user": new_user.to_dict()}), 201) 

@user_bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = validate_user(user_id)

    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'success': f'User {user.name} successfully deleted'})

@user_bp.route("/<user_id>", methods=["PATCH"])
def edit_user(user_id):
    user = validate_user(user_id) 
    request_body = request.get_json()

    if "name" in request_body:
        user.name = request_body["name"]        
    if "email" in request_body:
        user.email = request_body["email"]
    if "days_to_display" in request_body:
        user.days_to_display = request_body["days_to_display"]  
    if "menu_date" in request_body:
        user.menu_date = request_body["menu_date"]
    if "favorite" in request_body:
        user.favorite = request_body["favorite"]   
    db.session.commit()

    return {"updated user": user.to_dict()}

@user_bp.route("/<user_id>/recipe/<recipe_id>", methods=["PATCH"])
def add_recipe_to_user(user_id, recipe_id):
    user = validate_user(user_id) 
    recipe = validate_recipe(recipe_id)            
    request_body = request.get_json()      

    recipes_list = []    
    recipe.user = user 
    if "menu_date" in request_body:
        user.menu_date = request_body["menu_date"]
    if "favorite" in request_body:
        user.favorite = request_body["favorite"]
    recipes_list.append(recipe.recipe_id)

    db.session.commit()

    updatedUser = {
        "user_id": user_id,
        "name": user.name,
        "email": user.email,
        "days_to_display": user.days_to_display,
        "recipe_id": recipe_id,
        "menu_date": user.menu_date,
        "favorite": user.favorite
    }

    return make_response(jsonify(updatedUser)), 200

@user_bp.route("/<user_id>/recipes", methods=["GET"])
def get_recipes_per_user(user_id):
    user = validate_user(user_id)
    date_param = request.args.get("menu_date")

    if date_param:     
        user = User.query.get(user.menu_date==date_param)
        if not user.recipe:
            return {"warning": "no recipe for date"}           
        else:
            recipes_info = [recipe.to_dict() for recipe in user.recipe]            

    db.session.commit()

    return make_response(jsonify(recipes_info)), 200