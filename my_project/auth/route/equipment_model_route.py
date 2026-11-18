from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import equipment_model_controller
from my_project.auth.domain import EquipmentModel

equipment_model_bp = Blueprint("equipment_model", __name__, url_prefix="/equipment-model")


@equipment_model_bp.get("")
def get_all_equipment_model() -> Response:
    return make_response(jsonify(equipment_model_controller.find_all()), HTTPStatus.OK)


@equipment_model_bp.post("")
def create_equipment_model() -> Response:
    obj = EquipmentModel.create_from_dto(request.get_json())
    return make_response(jsonify(equipment_model_controller.create(obj)), HTTPStatus.CREATED)


@equipment_model_bp.get("/<int:equipment_model_id>")
def get_equipment_model(equipment_model_id: int) -> Response:
    return make_response(jsonify(equipment_model_controller.find_by_id(equipment_model_id)), HTTPStatus.OK)


@equipment_model_bp.put("/<int:equipment_model_id>")
def update_equipment_model(equipment_model_id: int) -> Response:
    obj = EquipmentModel.create_from_dto(request.get_json())
    return make_response(jsonify(equipment_model_controller.update(equipment_model_id, obj)), HTTPStatus.OK)


@equipment_model_bp.patch("/<int:equipment_model_id>")
def patch_equipment_model(equipment_model_id: int) -> Response:
    return make_response(jsonify(equipment_model_controller.patch(equipment_model_id, request.get_json())), HTTPStatus.OK)


@equipment_model_bp.delete("/<int:equipment_model_id>")
def delete_equipment_model(equipment_model_id: int) -> Response:
    equipment_model_controller.delete(equipment_model_id)
    return make_response(jsonify({"message": "EquipmentModel deleted"}), HTTPStatus.OK)
