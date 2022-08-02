from flask import Blueprint, request, jsonify, make_response
from app import db
from dotenv import load_dotenv
from app.models.user import User
from app.models.recipe import Recipe
from ..helpers.helper_functions import validate_user, validate_recipe
from sqlalchemy import and_

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
    db.session.commit()

    return {"updated user": user.to_dict()}

@user_bp.route("/<user_id>/recipe/<id>", methods=["PATCH"])
def add_recipe_to_user(user_id, id):
    user = validate_user(user_id) 
    recipe = validate_recipe(id)            
    request_body = request.get_json()      

    recipe.user = user 
    if "menu_date" in request_body:
        recipe.menu_date = request_body["menu_date"]
    if "favorite" in request_body:
        recipe.favorite = request_body["favorite"]

    db.session.commit()

    updatedUser = {
        "user_id": user_id,
        "name": user.name,
        "email": user.email,
        "days_to_display": user.days_to_display,
        "id": id,
        "menu_date": recipe.menu_date,
        "favorite": recipe.favorite
    }

    return make_response(jsonify(updatedUser)), 200