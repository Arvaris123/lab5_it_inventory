from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import office_controller
from my_project.auth.domain import Office

office_bp = Blueprint("office", __name__, url_prefix="/office")


@office_bp.get("")
def get_all_office() -> Response:
    return make_response(jsonify(office_controller.find_all()), HTTPStatus.OK)


@office_bp.post("")
def create_office() -> Response:
    obj = Office.create_from_dto(request.get_json())
    return make_response(jsonify(office_controller.create(obj)), HTTPStatus.CREATED)


@office_bp.get("/<int:office_id>")
def get_office(office_id: int) -> Response:
    return make_response(jsonify(office_controller.find_by_id(office_id)), HTTPStatus.OK)


@office_bp.put("/<int:office_id>")
def update_office(office_id: int) -> Response:
    obj = Office.create_from_dto(request.get_json())
    return make_response(jsonify(office_controller.update(office_id, obj)), HTTPStatus.OK)


@office_bp.patch("/<int:office_id>")
def patch_office(office_id: int) -> Response:
    return make_response(jsonify(office_controller.patch(office_id, request.get_json())), HTTPStatus.OK)


@office_bp.delete("/<int:office_id>")
def delete_office(office_id: int) -> Response:
    office_controller.delete(office_id)
    return make_response(jsonify({"message": "Office deleted"}), HTTPStatus.OK)


@office_bp.get("/city/<string:city>")
def get_offices_by_city(city: str) -> Response:
    return make_response(jsonify(office_controller.find_by_city(city)), HTTPStatus.OK)


@office_bp.get("/workplaces")
def get_all_offices_with_workplaces() -> Response:
    return make_response(jsonify(office_controller.find_all_with_workplaces()), HTTPStatus.OK)


@office_bp.get("/<int:office_id>/workplaces")
def get_office_workplaces(office_id: int) -> Response:
    return make_response(jsonify(office_controller.get_workplaces(office_id)), HTTPStatus.OK)


@office_bp.get("/<int:office_id>/equipment")
def get_office_equipment(office_id: int) -> Response:
    status = request.args.get("status")
    return make_response(jsonify(office_controller.get_equipment(office_id, status)), HTTPStatus.OK)
