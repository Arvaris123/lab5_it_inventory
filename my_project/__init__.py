from http import HTTPStatus

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DBAPIError, IntegrityError

db = SQLAlchemy()


def create_app(config: dict) -> Flask:
    app = Flask(__name__)
    app.json.ensure_ascii = False
    app.json.sort_keys = False

    mysql = config["mysql"]
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{mysql['user']}:{mysql['password']}"
        f"@{mysql['host']}:{mysql['port']}/{mysql['database']}?charset=utf8mb4"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from my_project.auth.route import register_routes
    register_routes(app)

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(error):
        db.session.rollback()
        return jsonify({"error": "Порушено обмеження БД", "details": str(error.orig)}), HTTPStatus.CONFLICT

    @app.errorhandler(DBAPIError)
    def handle_db_error(error):
        db.session.rollback()
        return jsonify({"error": "Некоректні дані", "details": str(error.orig)}), HTTPStatus.BAD_REQUEST

    @app.errorhandler(ValueError)
    def handle_value_error(error):
        db.session.rollback()
        return jsonify({"error": "Некоректний формат даних", "details": str(error)}), HTTPStatus.BAD_REQUEST

    @app.errorhandler(HTTPStatus.NOT_FOUND)
    def handle_not_found(error):
        return jsonify({"error": "Не знайдено"}), HTTPStatus.NOT_FOUND

    return app
