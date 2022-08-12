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

    if "favorite" in request_body:
        user_recipe.favorite = request_body["favorite"]
    if "menu_date" in request_body:
        user_recipe.menu_date = request_body["menu_date"]
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

    if user_recipes:
        for recipe in user_recipes:
            recipe = Recipe.query.get(user_recipes.rhash)
            recipe_dict = {
                "favorite": recipe.favorite,
                "id": recipe.id,
                "rhash": recipe.rhash,
                "uid": recipe.uid,
                "label": recipe.label
            }

            recipe_list.append(recipe_dict)
    db.session.commit()

    return make_response(jsonify(recipe_list)), 200

@ur_bp.route("/user/<uid>/date", methods=["GET"])
def get_user_menu_items(uid):
    user_recipe_dict = {}
    recipe_list = []
    start_date = request.args.get("start_date")
    date_str = start_date

    for i in range(7):
        user_recipe = UserRecipe.query.filter(and_(UserRecipe.uid == uid, UserRecipe.menu_date == date_str)).first()

        if user_recipe:
            recipe = Recipe.query.get(user_recipe.rhash)
            user_recipe_dict = {
            "id": user_recipe.id,
            "menu_date": user_recipe.menu_date,
            "rhash": user_recipe.rhash,
            "label": recipe.label,
            "image_url": recipe.image_url,
            "shareAs": recipe.shareAs
            }
        else:
            user_recipe_dict = {
                "id": "unkid" + str(i),
                "menu_date": date_str,
                "rhash": "unkrhash" + str(i),
                "image_url": "http://notfound.com",
                "shareAs": "http://notfound.com"
            }
        recipe_list.append(user_recipe_dict)

        date_dt = datetime.strptime(date_str, '%b %d %Y')
        nxt_day = date_dt + timedelta(days = 1)
        date_str = nxt_day.strftime('%b %d %Y')


    db.session.commit()

    return make_response(jsonify(recipe_list)), 200
