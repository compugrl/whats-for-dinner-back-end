from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from sqlalchemy import and_
from app.models.recipe import Recipe
from app.models.user import User
from app.models.user_recipe import UserRecipe
from ..helpers.helper_functions import validate_recipe, validate_user, validate_user_recipe
from datetime import datetime, timedelta

ur_bp = Blueprint("ur_bp", __name__, url_prefix="/ur")

# Not used in code. Needed for testing/debugging purposes
@ur_bp.route("", methods=["GET"])
def get_all_user_recipes():
    user_recipes = UserRecipe.query
    user_recipes = user_recipes.all()

    ur_response = []
    for user in user_recipes:
        ur_response.append(user.to_dict())

    return jsonify(ur_response)

@ur_bp.route("", methods=["POST"])
def create_user_recipe():
    request_body = request.get_json()
    if "uid" not in request_body:
        return make_response(jsonify(dict("User id missing")), 400)
    else:
        uid = request_body["uid"]

    if "rhash" not in request_body:
        return make_response(jsonify(dict("Recipe hash missing")), 400)
    else:
        rhash = request_body["rhash"]

    recipe = validate_recipe(rhash)
    user = validate_user(uid)
    request_body = request.get_json()
    new_user_recipe = UserRecipe.create(request_body)

    db.session.add(new_user_recipe)
    db.session.commit()

    return make_response(jsonify({"user_recipe": new_user_recipe.to_dict()}), 201)

@ur_bp.route("/<id>", methods=["PATCH"])
def update_user_recipe(id):
    user_recipe = validate_user_recipe(id)
    request_body = request.get_json()

    date_param = request.args.get("menu_date")
    fave_param = request.args.get("favorite")

    if date_param:
        user_recipe.menu_date = date_param
    if fave_param:
        user_recipe.favorite = fave_param

    db.session.commit()

    updatedUserRecipe = {
        "id": id,
        "uid": user_recipe.uid,
        "rhash": user_recipe.rhash,
        "menu_date": user_recipe.menu_date,
        "favorite": user_recipe.favorite
    }

    return make_response(jsonify(updatedUserRecipe)), 200

@ur_bp.route("/user/<uid>", methods=["GET"])
def get_recipes_per_user(uid):
    user = validate_user(uid)
    recipes_info = [recipe.to_dict() for recipe in user.recipe]

    db.session.commit()

    return make_response(jsonify(recipes_info)), 200

@ur_bp.route("/<id>", methods=["GET"])
def get_specific_user_recipe(id):
    user_recipe = validate_user_recipe(id)
    db.session.commit()

    return make_response(jsonify({"user_recipe": user_recipe.to_dict()}), 200)

@ur_bp.route("<id>", methods=["DELETE"])
def delete_user_recipe(id):
    user_recipe = validate_user_recipe(id)

    db.session.delete(user_recipe)
    db.session.commit()

    return jsonify({'success': f'User recipe {user_recipe.id} successfully deleted'})

@ur_bp.route("/user/<uid>/fave", methods=["GET"])
def get_user_favorite_recipes(uid):
    recipe_dict = {}
    recipe_list = []
    user_recipes = UserRecipe.query.filter(and_(UserRecipe.uid == uid, UserRecipe.favorite == True))

    for recipe in user_recipes:
        recipe_dict = {
            "favorite": recipe.favorite,
            "id": recipe.id,
            "menu_date": recipe.menu_date,
            "rhash": recipe.rhash,
            "uid": recipe.uid
        }

        recipe_list.append(recipe_dict)
    db.session.commit()

    return make_response(jsonify(recipe_list)), 200

@ur_bp.route("/user/<uid>/date", methods=["GET"])
def get_user_menu_items(uid):
    date_str = request.args.get("menu_date")
    get_menu_items_by_date(menu_date)        

    return make_response(jsonify(recipe_list)), 200
