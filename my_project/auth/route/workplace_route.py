from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import workplace_controller
from my_project.auth.domain import Workplace

workplace_bp = Blueprint("workplace", __name__, url_prefix="/workplace")


@workplace_bp.get("")
def get_all_workplace() -> Response:
    return make_response(jsonify(workplace_controller.find_all()), HTTPStatus.OK)


@workplace_bp.post("")
def create_workplace() -> Response:
    obj = Workplace.create_from_dto(request.get_json())
    return make_response(jsonify(workplace_controller.create(obj)), HTTPStatus.CREATED)


@workplace_bp.get("/<int:workplace_id>")
def get_workplace(workplace_id: int) -> Response:
    return make_response(jsonify(workplace_controller.find_by_id(workplace_id)), HTTPStatus.OK)


@workplace_bp.put("/<int:workplace_id>")
def update_workplace(workplace_id: int) -> Response:
    obj = Workplace.create_from_dto(request.get_json())
    return make_response(jsonify(workplace_controller.update(workplace_id, obj)), HTTPStatus.OK)


@workplace_bp.patch("/<int:workplace_id>")
def patch_workplace(workplace_id: int) -> Response:
    return make_response(jsonify(workplace_controller.patch(workplace_id, request.get_json())), HTTPStatus.OK)


@workplace_bp.delete("/<int:workplace_id>")
def delete_workplace(workplace_id: int) -> Response:
    workplace_controller.delete(workplace_id)
    return make_response(jsonify({"message": "Workplace deleted"}), HTTPStatus.OK)


@workplace_bp.get("/<int:workplace_id>/employees")
def get_workplace_employees(workplace_id: int) -> Response:
    return make_response(jsonify(workplace_controller.get_employees(workplace_id)), HTTPStatus.OK)
