from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import equipment_assignment_controller
from my_project.auth.domain import EquipmentAssignment

equipment_assignment_bp = Blueprint("equipment_assignment", __name__, url_prefix="/equipment-assignment")


@equipment_assignment_bp.get("")
def get_all_equipment_assignment() -> Response:
    return make_response(jsonify(equipment_assignment_controller.find_all()), HTTPStatus.OK)


@equipment_assignment_bp.post("")
def create_equipment_assignment() -> Response:
    obj = EquipmentAssignment.create_from_dto(request.get_json())
    return make_response(jsonify(equipment_assignment_controller.create(obj)), HTTPStatus.CREATED)


@equipment_assignment_bp.get("/<int:equipment_assignment_id>")
def get_equipment_assignment(equipment_assignment_id: int) -> Response:
    return make_response(jsonify(equipment_assignment_controller.find_by_id(equipment_assignment_id)), HTTPStatus.OK)


@equipment_assignment_bp.put("/<int:equipment_assignment_id>")
def update_equipment_assignment(equipment_assignment_id: int) -> Response:
    obj = EquipmentAssignment.create_from_dto(request.get_json())
    return make_response(jsonify(equipment_assignment_controller.update(equipment_assignment_id, obj)), HTTPStatus.OK)


@equipment_assignment_bp.patch("/<int:equipment_assignment_id>")
def patch_equipment_assignment(equipment_assignment_id: int) -> Response:
    return make_response(jsonify(equipment_assignment_controller.patch(equipment_assignment_id, request.get_json())), HTTPStatus.OK)


@equipment_assignment_bp.delete("/<int:equipment_assignment_id>")
def delete_equipment_assignment(equipment_assignment_id: int) -> Response:
    equipment_assignment_controller.delete(equipment_assignment_id)
    return make_response(jsonify({"message": "EquipmentAssignment deleted"}), HTTPStatus.OK)
