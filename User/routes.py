from flask import request
from User import bp
from models import User

from util import response
from util import not_found
from util import bad_request
from util import validate_auth

from .schemas import user_schema
from .schemas import users_schema
from .schemas import params_users_schema


def set_User(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        user = User.query.filter_by(id=id).first()
        if user is None:
            return not_found()
        return function(user)
    wrap.__name__ = function.__name__
    return wrap

#INICIAR GET
@bp.route('/', methods=['GET'])
@bp.response(200, users_schema)
def get_Users():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'desc')
    Users = User.get_by_page(order, page)
    return response(users_schema.dump(Users))

#INICIAR DETALLE ID
@bp.route('/<id>', methods=['GET'])
@set_User
def get_User(user):
    return response(user_schema.dump(user))

#INICIAR GUARDAR
@bp.route('/', methods=['POST'])
def create_User():
    json = request.get_json(force=True)
    error = params_users_schema.validate(json)
    if error:
        print(error)
        return bad_request()
    email = User.get_by_email(json['email'])
    if email is not None:
        return validate_auth('El email ya está siendo utilizado por otro usuario')
    username = User.get_by_username(json['username'])
    if username is not None:
        return validate_auth('El username ya está siendo utilizado por otro usuario')
    
    user = User.new(json['username'], json['email'], json['password'], json['rol_id'])
    user.set_password(json['password'])
    if user.save():
        return response(user_schema.dump(user))
    
    return bad_request()

#INICIAR ACTUALIZAR
@bp.route('/<id>', methods=['PUT'])
@set_User
def update_User(user):
    json = request.get_json(force=True)
    user.username = json.get('username', user.username)
    user.email = json.get('email', user.email)
    user.password = json.get('password', user.password)
    user.rol_id = json.get('rol_id', user.rol_id)
    if user.save():
        return response(user_schema.dump(user))

    return bad_request()

#INICIAR ELIMINAR
@bp.route('/<id>', methods=['DELETE'])
@set_User
def delete_User(user):
    if user.delete():
        return response(user_schema.dump(user))
    
    return bad_request()