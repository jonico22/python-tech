from flask import request
from auth import bp
from models import User
from flask_smorest import abort
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt,
    jwt_required,
)
from werkzeug.security import check_password_hash
from .schemas import login_schema
from blocklist import BLOCKLIST

@bp.route('/login', methods=['POST'])
def loginUser():
    json = request.get_json(force=True)
    user = User.query.filter(
            User.email == json['email']
        ).first()
    
    if user and check_password_hash(user.password, json['password']):    
        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)
        return {"access_token": access_token, "refresh_token": refresh_token}, 200
    abort(401, message="Invalid credentials.")

# Endpoint for revoking the current users access token. Save the JWTs unique
@bp.route('/logout', methods=['POST'])
@jwt_required()
def logoutUser():
    jti = get_jwt()["jti"]
    BLOCKLIST.add(jti)
    return {"message": "Successfully logged out"}, 200

@bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refreshUser():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, fresh=False)
    # Make it clear that when to add the refresh token to the blocklist will depend on the app design
    jti = get_jwt()["jti"]
    BLOCKLIST.add(jti)
    return {"access_token": new_token}, 200 