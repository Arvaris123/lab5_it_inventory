from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import equipment_controller
from my_project.auth.domain import Equipment

equipment_bp = Blueprint("equipment", __name__, url_prefix="/equipment")


@equipment_bp.get("")
def get_all_equipment() -> Response:
    return make_response(jsonify(equipment_controller.find_all()), HTTPStatus.OK)


@equipment_bp.post("")
def create_equipment() -> Response:
    obj = Equipment.create_from_dto(request.get_json())
    return make_response(jsonify(equipment_controller.create(obj)), HTTPStatus.CREATED)


@equipment_bp.get("/<int:equipment_id>")
def get_equipment(equipment_id: int) -> Response:
    return make_response(jsonify(equipment_controller.find_by_id(equipment_id)), HTTPStatus.OK)


@equipment_bp.put("/<int:equipment_id>")
def update_equipment(equipment_id: int) -> Response:
    obj = Equipment.create_from_dto(request.get_json())
    return make_response(jsonify(equipment_controller.update(equipment_id, obj)), HTTPStatus.OK)


@equipment_bp.patch("/<int:equipment_id>")
def patch_equipment(equipment_id: int) -> Response:
    return make_response(jsonify(equipment_controller.patch(equipment_id, request.get_json())), HTTPStatus.OK)


@equipment_bp.delete("/<int:equipment_id>")
def delete_equipment(equipment_id: int) -> Response:
    equipment_controller.delete(equipment_id)
    return make_response(jsonify({"message": "Equipment deleted"}), HTTPStatus.OK)


@equipment_bp.get("/<int:equipment_id>/assignments")
def get_equipment_assignments(equipment_id: int) -> Response:
    return make_response(jsonify(equipment_controller.get_assignments(equipment_id)), HTTPStatus.OK)
