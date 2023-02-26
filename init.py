from flask import Flask, jsonify, request
import os
from Rol import bp as rol_routes
from User import bp as user_routes
from Category import bp as category_routes
from Country import bp as country_routes
<<<<<<< HEAD
from Event import bp as event_routes
=======
from flask_smorest import Api
>>>>>>> 59cf0e6 (add flask-smorest)

def create_app():
    # creates an application that is named after the name of the file
    app = Flask(__name__)
    app.config["API_TITLE"] = "Tech Latam REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api = Api(app)

<<<<<<< HEAD
    app.register_blueprint(rol_routes, url_prefix='/api/v1/roles')
    app.register_blueprint(user_routes, url_prefix='/api/v1/user')
    app.register_blueprint(category_routes, url_prefix='/api/v1/categorias')
    app.register_blueprint(country_routes, url_prefix='/api/v1/paises')
    app.register_blueprint(event_routes, url_prefix='/api/v1/eventos')
=======
    api.register_blueprint(rol_routes, url_prefix='/api/v1/roles')
    api.register_blueprint(user_routes, url_prefix='/api/v1/user')
    api.register_blueprint(category_routes, url_prefix='/api/v1/categorias')
    api.register_blueprint(country_routes, url_prefix='/api/v1/paises')
>>>>>>> 59cf0e6 (add flask-smorest)

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
