from flask import Blueprint, request, jsonify, make_response
from app import db
from dotenv import load_dotenv
from app.models.user import User
from app.models.recipe import Recipe
from app.models.user_recipe import UserRecipe
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

@user_bp.route("/<uid>", methods=["GET"])
def get_one_user(uid):
    user = validate_user(uid)    
    return {"user": user.to_dict()}

@user_bp.route("", methods=["POST"])
def create_user():
    request_body = request.get_json()
    if "uid" not in request_body:
        return make_response(jsonify(dict("User must have a id")), 400)
    if "name" not in request_body:
        return make_response(jsonify(dict("User must have a name")), 400)
    if "email" not in request_body:
        return make_response(jsonify(dict("User must have a valid email address")), 400)
    
    new_user = User.create(request_body)
    
    db.session.add(new_user)
    db.session.commit()

    return make_response(jsonify({"user": new_user.to_dict()}), 201) 

@user_bp.route("/<uid>", methods=["DELETE"])
def delete_user(uid):
    user = validate_user(uid)

    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'success': f'User {user.name} successfully deleted'})

@user_bp.route("/<uid>", methods=["PATCH"])
def edit_user(uid):
    user = validate_user(uid) 
    request_body = request.get_json()

    if "uid" in request_body:
        user.name = request_body["uid"]        
    if "name" in request_body:
        user.name = request_body["name"]        
    if "email" in request_body:
        user.email = request_body["email"]  
    db.session.commit()

    return {"updated user": user.to_dict()}