from flask import request
from Rol import bp
from models import Rol

from util import response
from util import not_found
from util import bad_request

from .schemas import rol_schema
from .schemas import roles_schema
from .schemas import params_roles_schema


def set_Rol(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        rol = Rol.query.filter_by(id=id).first()
        if rol is None:
            return not_found()
        return function(rol)
    wrap.__name__ = function.__name__
    return wrap

#INICIAR GET
@bp.route('/', methods=['GET'])
def get_Rols():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'desc')
    Rols = Rol.get_by_page(order, page)
    return response(roles_schema.dump(Rols))

#INICIAR DETALLE ID
@bp.route('/<id>', methods=['GET'])
@set_Rol
def get_rol(rol):
    return response(rol_schema.dump(rol))

#INICIAR GUARDAR
@bp.route('/', methods=['POST'])
def create_rol():
    json = request.get_json(force=True)
    print(json)
    print(json['name'])
    error = params_roles_schema.validate(json)
    if error:
        print(error)
        return bad_request()
    rol = Rol.new(json['name'])
    if rol.save():
        return response(rol_schema.dump(rol))
    
    return bad_request()

#INICIAR ACTUALIZAR
@bp.route('/<id>', methods=['PUT'])
@set_Rol
def update_rol(rol):
    json = request.get_json(force=True)
    rol.name = json.get('name', rol.name)
    if rol.save():
        return response(rol_schema.dump(rol))

    return bad_request()

#INICIAR ELIMINAR
@bp.route('/<id>', methods=['DELETE'])
@set_Rol
def delete_rol(rol):
    if rol.delete():
        return response(rol_schema.dump(rol))
    return bad_request()