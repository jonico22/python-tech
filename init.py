from flask import Flask, jsonify, request
import os
from Rol import bp as rol_routes
from User import bp as user_routes
from Category import bp as category_routes
from Country import bp as country_routes
from Event import bp as event_routes
from Recommendation import bp as recommendation_routes
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST
from auth import bp as auth_routes
from flask_cors import CORS

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
    app.config["JWT_SECRET_KEY"] = "tech"
    jwt = JWTManager(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    api = Api(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )


    @app.errorhandler(404)
    def not_found(error):
        app.logger.info(
            f"404 => user tried to access route {request.full_path}"
        )
        return jsonify({
            "msg": "ruta no permitida",
            "success": False,
            "data": []
        }), 404
    
    api.register_blueprint(rol_routes, url_prefix='/api/v1/roles')
    api.register_blueprint(user_routes, url_prefix='/api/v1/user')
    api.register_blueprint(category_routes, url_prefix='/api/v1/categorias')
    api.register_blueprint(country_routes, url_prefix='/api/v1/paises')
    api.register_blueprint(event_routes, url_prefix='/api/v1/eventos')
    api.register_blueprint(recommendation_routes, url_prefix='/api/v1/recomendaciones')
    api.register_blueprint(auth_routes, url_prefix='/api/v1/auth')
    
    return app
