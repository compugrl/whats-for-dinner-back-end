from flask import jsonify, make_response, abort
from app.models.user import User
from app.models.recipe import Recipe
from app.models.shopping_list import Shopping_list

def parse_recipe(input_data):
    recipe_list = []
    recipe_dict = {}
    input_data = input_data.json()
    hits = input_data["hits"]

    for hit in hits:
        label = hit["recipe"]["label"]
        image_url = hit["recipe"]["image"]
        shareAs = hit["recipe"]["shareAs"]

        uri = hit["recipe"]["uri"]
        start_pos = uri.find("#") + 8
        hash = uri[start_pos::]

        recipe_dict = {
            "hash": hash,
            "label": label,
            "image_url": image_url,
            "shareAs": shareAs,
        }
        recipe_list.append(recipe_dict)

    return recipe_list

def parse_ingredients(input_data):
    ingredient_list = []
    ingredients = input_data["recipe"]["ingredients"]
    for ingredient in ingredients:
        food = ingredient["text"]
        ingredient_list.append(food)

    return ingredient_list

def user_recipe_to_dict(user):
    for recipe in user:
        user_recipe = {
            "id": id
        }
    return user_recipe

def validate_user(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        abort(make_response(jsonify({'error': f'Invalid user id: {user_id}'}), 400))

    user = User.query.get(user_id)

    if not user:
        return abort(make_response(jsonify(f"User {user_id} not found"), 404))

    return user

def validate_recipe(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response(jsonify({'error': f'Invalid recipe id: {id}'}), 400))

    recipe = Recipe.query.get(id)

    if not recipe:
        return abort(make_response(jsonify(f"Recipe {id} not found"), 404))

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
