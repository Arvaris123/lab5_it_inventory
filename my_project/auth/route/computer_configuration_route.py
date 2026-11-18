from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import computer_configuration_controller
from my_project.auth.domain import ComputerConfiguration

computer_configuration_bp = Blueprint("computer_configuration", __name__, url_prefix="/computer-configuration")


@computer_configuration_bp.get("")
def get_all_computer_configuration() -> Response:
    return make_response(jsonify(computer_configuration_controller.find_all()), HTTPStatus.OK)


@computer_configuration_bp.post("")
def create_computer_configuration() -> Response:
    obj = ComputerConfiguration.create_from_dto(request.get_json())
    return make_response(jsonify(computer_configuration_controller.create(obj)), HTTPStatus.CREATED)


@computer_configuration_bp.get("/<int:computer_configuration_id>")
def get_computer_configuration(computer_configuration_id: int) -> Response:
    return make_response(jsonify(computer_configuration_controller.find_by_id(computer_configuration_id)), HTTPStatus.OK)


@computer_configuration_bp.put("/<int:computer_configuration_id>")
def update_computer_configuration(computer_configuration_id: int) -> Response:
    obj = ComputerConfiguration.create_from_dto(request.get_json())
    return make_response(jsonify(computer_configuration_controller.update(computer_configuration_id, obj)), HTTPStatus.OK)


@computer_configuration_bp.patch("/<int:computer_configuration_id>")
def patch_computer_configuration(computer_configuration_id: int) -> Response:
    return make_response(jsonify(computer_configuration_controller.patch(computer_configuration_id, request.get_json())), HTTPStatus.OK)


@computer_configuration_bp.delete("/<int:computer_configuration_id>")
def delete_computer_configuration(computer_configuration_id: int) -> Response:
    computer_configuration_controller.delete(computer_configuration_id)
    return make_response(jsonify({"message": "ComputerConfiguration deleted"}), HTTPStatus.OK)
