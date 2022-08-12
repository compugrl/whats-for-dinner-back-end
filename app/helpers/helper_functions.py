from flask import jsonify, make_response, abort
from app.models.user import User
from app.models.recipe import Recipe
from app.models.shopping_list import Shopping_list
from app.models.user_recipe import UserRecipe
from app import db
from sqlalchemy import and_

def parse_recipe(input_data):
    recipe_list = []
    recipe_dict = {}
    hits = input_data["hits"]

    for hit in hits:
        label = hit["recipe"]["label"]
        image_url = hit["recipe"]["image"]
        shareAs = hit["recipe"]["shareAs"]

        uri = hit["recipe"]["uri"]
        start_pos = uri.find("#") + 8
        rhash = uri[start_pos::]

        recipe_dict = {
            "rhash": rhash,
            "label": label,
            "image_url": image_url,
            "shareAs": shareAs
        }
        recipe_list.append(recipe_dict)

    return recipe_list

def parse_ingredients(input_data):
    ingredient_list = []
    input_data = input_data.json()
    ingredients = input_data["recipe"]["ingredients"]
    for ingredient in ingredients:
        food = ingredient["food"]
        ingredient_list.append(food)

    return ingredient_list

def validate_user(uid):
    user = User.query.get(uid)

    if not user:
        return abort(make_response(jsonify(f"User {uid} not found"), 404))

    return user

def validate_recipe(rhash):
    recipe = Recipe.query.get(rhash)

    if not recipe:
        return abort(make_response(jsonify(f"Recipe {rhash} not found"), 404))

    return recipe

def validate_shopping_list(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response(jsonify({'error': f'Invalid shopping list id: {id}'}), 400))

    shopping_list = Shopping_list.query.get(id)

    if not shopping_list:
        return abort(make_response(jsonify(f"Shopping list ingredient {id} not found"), 404))

    return shopping_list

def validate_user_recipe(id):
    user_recipe = UserRecipe.query.get(id)

    if not user_recipe:
        return abort(make_response(jsonify(f"User Recipe {id} not found"), 404))

    return user_recipe
