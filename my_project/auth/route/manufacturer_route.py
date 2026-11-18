from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import manufacturer_controller
from my_project.auth.domain import Manufacturer

manufacturer_bp = Blueprint("manufacturer", __name__, url_prefix="/manufacturer")


@manufacturer_bp.get("")
def get_all_manufacturer() -> Response:
    return make_response(jsonify(manufacturer_controller.find_all()), HTTPStatus.OK)


@manufacturer_bp.post("")
def create_manufacturer() -> Response:
    obj = Manufacturer.create_from_dto(request.get_json())
    return make_response(jsonify(manufacturer_controller.create(obj)), HTTPStatus.CREATED)


@manufacturer_bp.get("/<int:manufacturer_id>")
def get_manufacturer(manufacturer_id: int) -> Response:
    return make_response(jsonify(manufacturer_controller.find_by_id(manufacturer_id)), HTTPStatus.OK)


@manufacturer_bp.put("/<int:manufacturer_id>")
def update_manufacturer(manufacturer_id: int) -> Response:
    obj = Manufacturer.create_from_dto(request.get_json())
    return make_response(jsonify(manufacturer_controller.update(manufacturer_id, obj)), HTTPStatus.OK)


@manufacturer_bp.patch("/<int:manufacturer_id>")
def patch_manufacturer(manufacturer_id: int) -> Response:
    return make_response(jsonify(manufacturer_controller.patch(manufacturer_id, request.get_json())), HTTPStatus.OK)


@manufacturer_bp.delete("/<int:manufacturer_id>")
def delete_manufacturer(manufacturer_id: int) -> Response:
    manufacturer_controller.delete(manufacturer_id)
    return make_response(jsonify({"message": "Manufacturer deleted"}), HTTPStatus.OK)


@manufacturer_bp.get("/<int:manufacturer_id>/models")
def get_manufacturer_models(manufacturer_id: int) -> Response:
    return make_response(jsonify(manufacturer_controller.get_models(manufacturer_id)), HTTPStatus.OK)
