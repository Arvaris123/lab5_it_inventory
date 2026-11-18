from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import employee_controller
from my_project.auth.domain import Employee

employee_bp = Blueprint("employee", __name__, url_prefix="/employee")


@employee_bp.get("")
def get_all_employee() -> Response:
    return make_response(jsonify(employee_controller.find_all()), HTTPStatus.OK)


@employee_bp.post("")
def create_employee() -> Response:
    obj = Employee.create_from_dto(request.get_json())
    return make_response(jsonify(employee_controller.create(obj)), HTTPStatus.CREATED)


@employee_bp.get("/<int:employee_id>")
def get_employee(employee_id: int) -> Response:
    return make_response(jsonify(employee_controller.find_by_id(employee_id)), HTTPStatus.OK)


@employee_bp.put("/<int:employee_id>")
def update_employee(employee_id: int) -> Response:
    obj = Employee.create_from_dto(request.get_json())
    return make_response(jsonify(employee_controller.update(employee_id, obj)), HTTPStatus.OK)


@employee_bp.patch("/<int:employee_id>")
def patch_employee(employee_id: int) -> Response:
    return make_response(jsonify(employee_controller.patch(employee_id, request.get_json())), HTTPStatus.OK)


@employee_bp.delete("/<int:employee_id>")
def delete_employee(employee_id: int) -> Response:
    employee_controller.delete(employee_id)
    return make_response(jsonify({"message": "Employee deleted"}), HTTPStatus.OK)


@employee_bp.get("/last-name/<string:last_name>")
def get_employees_by_last_name(last_name: str) -> Response:
    return make_response(jsonify(employee_controller.find_by_last_name(last_name)), HTTPStatus.OK)


@employee_bp.get("/workplaces")
def get_all_employees_with_workplaces() -> Response:
    return make_response(jsonify(employee_controller.find_all_with_workplaces()), HTTPStatus.OK)


@employee_bp.get("/<int:employee_id>/workplaces")
def get_employee_workplaces(employee_id: int) -> Response:
    return make_response(jsonify(employee_controller.get_workplaces(employee_id)), HTTPStatus.OK)


@employee_bp.get("/<int:employee_id>/assignments")
def get_employee_assignments(employee_id: int) -> Response:
    return make_response(jsonify(employee_controller.get_assignments(employee_id)), HTTPStatus.OK)
