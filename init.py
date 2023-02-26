from flask import Flask, jsonify, request
import os
from Rol import bp as rol_routes
from User import bp as user_routes

def create_app():
    # creates an application that is named after the name of the file
    app = Flask(__name__)
    # alternative configuration based on if is test env or not
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(rol_routes, url_prefix='/api/v1/roles')
    app.register_blueprint(user_routes, url_prefix='/api/v1/user')

    @app.errorhandler(404)
    def not_found(error):
        app.logger.info(
            f"404 => user tried to access route {request.full_path}"
        )
        return jsonify({
            "msg": "ruta no permitida",
            "success": False,
            "data": None
        }), 404

    return app