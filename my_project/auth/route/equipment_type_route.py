from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import equipment_type_controller
from my_project.auth.domain import EquipmentType

equipment_type_bp = Blueprint("equipment_type", __name__, url_prefix="/equipment-type")


@equipment_type_bp.get("")
def get_all_equipment_type() -> Response:
    return make_response(jsonify(equipment_type_controller.find_all()), HTTPStatus.OK)


@equipment_type_bp.post("")
def create_equipment_type() -> Response:
    obj = EquipmentType.create_from_dto(request.get_json())
    return make_response(jsonify(equipment_type_controller.create(obj)), HTTPStatus.CREATED)


@equipment_type_bp.get("/<int:equipment_type_id>")
def get_equipment_type(equipment_type_id: int) -> Response:
    return make_response(jsonify(equipment_type_controller.find_by_id(equipment_type_id)), HTTPStatus.OK)


@equipment_type_bp.put("/<int:equipment_type_id>")
def update_equipment_type(equipment_type_id: int) -> Response:
    obj = EquipmentType.create_from_dto(request.get_json())
    return make_response(jsonify(equipment_type_controller.update(equipment_type_id, obj)), HTTPStatus.OK)


@equipment_type_bp.patch("/<int:equipment_type_id>")
def patch_equipment_type(equipment_type_id: int) -> Response:
    return make_response(jsonify(equipment_type_controller.patch(equipment_type_id, request.get_json())), HTTPStatus.OK)


@equipment_type_bp.delete("/<int:equipment_type_id>")
def delete_equipment_type(equipment_type_id: int) -> Response:
    equipment_type_controller.delete(equipment_type_id)
    return make_response(jsonify({"message": "EquipmentType deleted"}), HTTPStatus.OK)


@equipment_type_bp.get("/<int:equipment_type_id>/models")
def get_equipment_type_models(equipment_type_id: int) -> Response:
    return make_response(jsonify(equipment_type_controller.get_models(equipment_type_id)), HTTPStatus.OK)
