from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import employee_workplace_controller
from my_project.auth.domain import EmployeeWorkplace

employee_workplace_bp = Blueprint("employee_workplace", __name__, url_prefix="/employee-workplace")


@employee_workplace_bp.get("")
def get_all_employee_workplace() -> Response:
    return make_response(jsonify(employee_workplace_controller.find_all()), HTTPStatus.OK)


@employee_workplace_bp.post("")
def create_employee_workplace() -> Response:
    obj = EmployeeWorkplace.create_from_dto(request.get_json())
    return make_response(jsonify(employee_workplace_controller.create(obj)), HTTPStatus.CREATED)


@employee_workplace_bp.get("/<int:employee_id>/<int:workplace_id>")
def get_employee_workplace(employee_id: int, workplace_id: int) -> Response:
    key = (employee_id, workplace_id)
    return make_response(jsonify(employee_workplace_controller.find_by_id(key)), HTTPStatus.OK)


@employee_workplace_bp.put("/<int:employee_id>/<int:workplace_id>")
def update_employee_workplace(employee_id: int, workplace_id: int) -> Response:
    key = (employee_id, workplace_id)
    obj = EmployeeWorkplace.create_from_dto(request.get_json())
    return make_response(jsonify(employee_workplace_controller.update(key, obj)), HTTPStatus.OK)


@employee_workplace_bp.delete("/<int:employee_id>/<int:workplace_id>")
def delete_employee_workplace(employee_id: int, workplace_id: int) -> Response:
    employee_workplace_controller.delete((employee_id, workplace_id))
    return make_response(jsonify({"message": "EmployeeWorkplace deleted"}), HTTPStatus.OK)
