from flask import Flask, jsonify

from .office_route import office_bp
from .workplace_route import workplace_bp
from .employee_route import employee_bp
from .employee_workplace_route import employee_workplace_bp
from .manufacturer_route import manufacturer_bp
from .equipment_type_route import equipment_type_bp
from .equipment_model_route import equipment_model_bp
from .computer_configuration_route import computer_configuration_bp
from .equipment_route import equipment_bp
from .equipment_assignment_route import equipment_assignment_bp
from .procedure_route import procedure_bp


def register_routes(app: Flask) -> None:
    @app.get("/")
    def hello():
        return jsonify({"message": "IT inventory API (lab 4, variant 47)"})

    app.register_blueprint(office_bp)
    app.register_blueprint(workplace_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(employee_workplace_bp)
    app.register_blueprint(manufacturer_bp)
    app.register_blueprint(equipment_type_bp)
    app.register_blueprint(equipment_model_bp)
    app.register_blueprint(computer_configuration_bp)
    app.register_blueprint(equipment_bp)
    app.register_blueprint(equipment_assignment_bp)
    app.register_blueprint(procedure_bp)
