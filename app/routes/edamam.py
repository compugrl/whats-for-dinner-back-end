
from flask import Blueprint, request, jsonify, make_response
import os
from dotenv import load_dotenv
import requests
from ..helpers.helper_functions import parse_recipe, parse_ingredients

load_dotenv()

edamam_bp = Blueprint("edamam_bp", __name__, url_prefix='/search')

recipe_key = os.environ.get("RECIPE_KEY")
recipe_app = os.environ.get("RECIPE_APP")

@edamam_bp.route("", methods=["GET"])
def get_recipe():
    params = {
        "app_key": recipe_key, 
        "app_id": recipe_app, 
        "type": "public", 
        "mealType": "Dinner", 
        "random": "true", 
        "format": "json",
        }

    diet_lbl = 'diet'
    health_lbl = 'health'
    cuisine_lbl = 'cuisine'

    ingredient_query = request.args.get("q")
    if not ingredient_query:
        return {"message": "You must provide an ingredient to search for"}
    else:
        params["q"] = ingredient_query

    ingr_limit = request.args.get("ingr")
    if ingr_limit:
        params["ingr"] = f'1-{ingr_limit}'

    time = request.args.get("time")    
    if time:
        params["time"] = time

    excluded = request.args.get("excluded")
    if excluded:
        params["excluded"] = excluded

    diet_val = request.args.get("diet")
    if diet_val:
        if len(diet_val) > 1:
            diet_lbl = 'diets'
            params[diet_lbl] = diet_val

    health_val = request.args.get("health")
    if health_val:
        if len(health_val) > 1:
            health_lbl = 'healths'
            params[health_lbl] = health_val

    cuisine_val = request.args.get("cuisine")
    if cuisine_val:
        if len(cuisine_val) > 1:
            cuisine_lbl = 'cuisines'
            params[cuisine_lbl] = cuisine_val

    response = requests.get(f"https://api.edamam.com/api/recipes/v2",
        params
    )    

    data = response.json()
    new_data = parse_recipe(data)
    return make_response(jsonify(new_data)), 200

@edamam_bp.route("/<rhash>", methods=["GET"])
def get_specific_recipe(rhash):
    params = {
        "app_key": recipe_key,
        "app_id": recipe_app,
        "type": "public",
        "format": "json"
        }

    response = requests.get(
        f"https://api.edamam.com/api/recipes/v2/{rhash}",
        params
    )

    data = response.json()
    return data

@edamam_bp.route("/<rhash>/ingr", methods=["GET"])
def get_specific_recipe_ingr(rhash):
    params = {
        "app_key": recipe_key,
        "app_id": recipe_app,
        "type": "public",
        "format": "json",
        "field": "ingredients"
        }

    # response = requests.get(
    first_response = requests.get(
        f"https://api.edamam.com/api/recipes/v2/{rhash}",
        params
    )

    # data = response.json()
    # return data

    response = parse_ingredients(first_response)
    return make_response(jsonify(response)), 200