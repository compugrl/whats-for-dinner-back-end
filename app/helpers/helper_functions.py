from flask import jsonify, make_response, abort
from app.models.user import User
from app.models.recipe import Recipe
from app.models.shopping_list import Shopping_list

def parse_recipe(input_data):
    recipe_dict = {}
    label = input_data["recipe"]["label"]

    uri = input_data["recipe"]["uri"]
    start_pos = uri.find("#") + 8
    hash = uri[start_pos::]
    
    image_tnail = input_data["recipe"]["images"]["THUMBNAIL"]["url"]
    image_sm = input_data["recipe"]["images"]["SMALL"]["url"]

    recipe_dict[hash] = {
        "label": label,
        "image_tnail": image_tnail,
        "image_sm": image_sm,
    }

    return recipe_dict

def parse_ingredients(input_data):
    ingredient_list = []
    ingredients = input_data["recipe"]["ingredients"]
    for ingredient in ingredients:
        food = ingredient["text"]
        ingredient_list.append(food)

    return ingredient_list

def validate_user(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        abort(make_response(jsonify({'error': f'Invalid user id: {user_id}'}), 400))

    user = User.query.get(user_id)

    if not user:
        return abort(make_response(jsonify(f"User {user_id} not found"), 404))
    
    return user

def validate_recipe(recipe_id):
    try:
        recipe_id = int(recipe_id)
    except ValueError:
        abort(make_response(jsonify({'error': f'Invalid recipe id: {recipe_id}'}), 400))

    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return abort(make_response(jsonify(f"Recipe {recipe_id} not found"), 404))
    
    return recipe

def validate_shopping_list(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response(jsonify({'error': f'Invalid shopping list id: {id}'}), 400))

    shopping_list = Shopping_list.query.get(id)

    if not shopping_list:
        return abort(make_response(jsonify(f"Shopping list item {id} not found"), 404))

    return shopping_list