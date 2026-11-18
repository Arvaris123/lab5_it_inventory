from http import HTTPStatus

from flask import Blueprint, Response, jsonify, make_response, request

from my_project.auth.controller import procedure_controller

procedure_bp = Blueprint("procedure", __name__, url_prefix="/procedure")


@procedure_bp.post("/insert-manufacturer")
def insert_manufacturer() -> Response:
    data = request.get_json()
    procedure_controller.insert_manufacturer(data.get("name"), data.get("country"))
    return make_response(jsonify({"message": "Manufacturer inserted"}), HTTPStatus.CREATED)


@procedure_bp.post("/add-employee-workplace")
def add_employee_workplace() -> Response:
    data = request.get_json()
    procedure_controller.add_employee_workplace(data.get("last_name"), data.get("first_name"), data.get("code"))
    return make_response(jsonify({"message": "Employee workplace inserted"}), HTTPStatus.CREATED)


@procedure_bp.post("/insert-noname-types")
def insert_noname_types() -> Response:
    procedure_controller.insert_noname_types()
    return make_response(jsonify({"message": "10 Noname rows inserted"}), HTTPStatus.CREATED)


@procedure_bp.get("/avg-ram")
def show_avg_ram() -> Response:
    return make_response(jsonify({"avg_ram_gb": procedure_controller.show_avg_ram()}), HTTPStatus.OK)


@procedure_bp.post("/split-office")
def split_office() -> Response:
    procedure_controller.split_office()
    return make_response(jsonify({"message": "Office tables created"}), HTTPStatus.CREATED)
