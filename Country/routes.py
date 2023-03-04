from flask import request
from Country import bp
from models import Country

from util import response
from util import not_found
from util import bad_request

from .schemas import country_schema
from .schemas import countries_schema
from .schemas import params_countries_schema
from flask_jwt_extended import jwt_required

def set_Country(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        country = Country.query.filter_by(id=id).first()
        if country is None:
            return not_found()
        return function(country)
    wrap.__name__ = function.__name__
    return wrap

#INICIAR GET
@bp.route('/', methods=['GET'])
def get_Country():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'desc')
    Countries = Country.get_by_page(order, page)
    return response(countries_schema.dump(Countries))

#INICIAR DETALLE ID
@bp.route('/<id>', methods=['GET'])
@set_Country
def get_country(country):
    return response(country_schema.dump(country))

#INICIAR GUARDAR
@bp.route('/', methods=['POST'])
@jwt_required()
def create_country():
    json = request.get_json(force=True)
    error = params_countries_schema.validate(json)
    if error:
        print(error)
        return bad_request()
    country = Country.new(json['name'], json['code'])
    if country.save():
        return response(country_schema.dump(country))
    
    return bad_request()

#INICIAR ACTUALIZAR
@bp.route('/<id>', methods=['PUT'])
@jwt_required()
@set_Country
def update_country(country):
    json = request.get_json(force=True)
    country.name = json.get('name', country.name)
    country.code = json.get('code', country.code)
    if country.save():
        return response(country_schema.dump(country))

    return bad_request()

#INICIAR ELIMINAR
@bp.route('/<id>', methods=['DELETE'])
@jwt_required()
@set_Country
def delete_country(country):
    if country.delete():
        return response(country_schema.dump(country))
    return bad_request()
