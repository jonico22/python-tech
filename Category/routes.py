from flask import request
from Category import bp
from models import Category

from util import response
from util import not_found
from util import bad_request

from .schemas import category_schema
from .schemas import categories_schema
from .schemas import params_categories_schema

from flask_jwt_extended import jwt_required

def set_Category(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        category = Category.query.filter_by(id=id).first()
        if category is None:
            return not_found()
        return function(category)
    wrap.__name__ = function.__name__
    return wrap

#INICIAR GET
@bp.route('/', methods=['GET'])
def get_Categories():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'desc')
    Categories = Category.get_by_page(order, page)
    return response(categories_schema.dump(Categories))

#INICIAR DETALLE ID
@bp.route('/<id>', methods=['GET'])
@set_Category
def get_category(category):
    return response(category_schema.dump(category))

#INICIAR GUARDAR
@bp.route('/', methods=['POST'])
@jwt_required()
def create_category():
    json = request.get_json(force=True)
    error = params_categories_schema.validate(json)
    if error:
        print(error)
        return bad_request()
    category = Category.new(json['name'])
    if category.save():
        return response(category_schema.dump(category))
    
    return bad_request()

#INICIAR ACTUALIZAR
@bp.route('/<id>', methods=['PUT'])
@jwt_required()
@set_Category
def update_category(category):
    json = request.get_json(force=True)
    category.name = json.get('name', category.name)
    if category.save():
        return response(category_schema.dump(category))

    return bad_request()

#INICIAR ELIMINAR
@bp.route('/<id>', methods=['DELETE'])
@jwt_required()
@set_Category
def delete_category(category):
    if category.delete():
        return response(category_schema.dump(category))
    return bad_request()
