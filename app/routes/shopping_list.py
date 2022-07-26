from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.shopping_list import Shopping_list
from ..helpers.helper_functions import validate_shopping_list, validate_user
from sqlalchemy import asc, desc

shopping_list_bp = Blueprint('shopping_list', __name__, url_prefix='/shopping_list')

@shopping_list_bp.route("/<user_id>", methods=["POST"])
def create_shopping_list(user_id):
    request_body = request.get_json()
    new_shopping_list = Shopping_list(
        item = request_body["item"],
        user_id = user_id,
        completed = request_body["completed"]
        )
    
    if "item" not in request_body:
        return make_response(jsonify(dict("Item must be supplied")), 400)
    if "completed" not in request_body:
        return make_response(jsonify(dict("List requires 'completed' field")), 400)

    db.session.add(new_shopping_list)
    db.session.commit()
    shopping_list = Shopping_list.query.get(int(new_shopping_list.id))

    return make_response({"shopping_list": shopping_list.to_dict()}, 201)

@shopping_list_bp.route("/<user_id>/items", methods=["GET"])
def get_all_items_for_user(user_id):
    list_info = []
    user = validate_user(user_id)
    list_info = [item.to_dict() for item in user.shopping_list]
    return make_response(jsonify(list_info)), 200

@shopping_list_bp.route("/<id>", methods=["GET"])
def get_shopping_list_item(id):
    shopping_list = validate_shopping_list(id)
    return {"shopping_list": shopping_list.to_dict()}

@shopping_list_bp.route("/<user_id>/item/<id>", methods=["PATCH"])
def edit_list_item(user_id, id):
    user = validate_user(user_id)
    shopping_list = validate_shopping_list(id)
    request_body = request.get_json()

    if "item" in request_body:
        shopping_list.item = request_body["item"]        
    if "completed" in request_body:
        shopping_list.completed = request_body["completed"] 
    db.session.commit()

    return {"updated list": shopping_list.to_dict()}

@shopping_list_bp.route("/<id>", methods=["DELETE"])
def delete_shopping_list_item(id):
    shopping_list = validate_shopping_list(id)
    db.session.delete(shopping_list)
    db.session.commit()

    return jsonify({'success': f'Shopping list item: {shopping_list.item} successfully deleted'})
