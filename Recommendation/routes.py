from flask import request
from Recommendation import bp
from models import Recommendation

from util import response
from util import not_found
from util import bad_request
from util import validate_auth

from .schemas import recommendation_schema
from .schemas import recommendations_schema
from .schemas import params_recommendations_schema


def set_Recommendation(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        recommendation = Recommendation.query.filter_by(id=id).first()
        if recommendation is None:
            return not_found()
        return function(recommendation)
    wrap.__name__ = function.__name__
    return wrap

#INICIAR GET
@bp.route('/', methods=['GET'])
def get_Recommendations():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'desc')
    Recommendations = Recommendation.get_by_page(order, page)
    return response(recommendations_schema.dump(Recommendations))

#INICIAR DETALLE ID
@bp.route('/<id>', methods=['GET'])
@set_Recommendation
def get_Recommendation(recommendation):
    return response(recommendation_schema.dump(recommendation))

#INICIAR GUARDAR
@bp.route('/', methods=['POST'])
def create_recommendation():
    json = request.get_json(force=True)
    error = params_recommendations_schema.validate(json)
    if error:
        print(error)
        return bad_request()
    recommendation = Recommendation.new(json['title'], json['description'], json['user_id'], json['event_id'], json['category_id']) 
    if recommendation.save():
        return response(recommendation_schema.dump(recommendation))
    
    return bad_request()

#INICIAR ACTUALIZAR
@bp.route('/<id>', methods=['PUT'])
@set_Recommendation
def update_Recommendation(recommendation):
    json = request.get_json(force=True)
    recommendation.title = json.get('title', recommendation.title)
    recommendation.description = json.get('description', recommendation.description)
    recommendation.user_id = json.get('user_id', recommendation.user_id)  
    recommendation.event_id = json.get('event_id', recommendation.event_id)
    recommendation.category_id = json.get('category_id', recommendation.category_id)     
    if recommendation.save():
        return response(recommendation_schema.dump(recommendation))

    return bad_request()

#INICIAR ELIMINAR
@bp.route('/<id>', methods=['DELETE'])
@set_Recommendation
def delete_Recommendation(recommendation):
    if recommendation.delete():
        return response(recommendation_schema.dump(recommendation))
    return bad_request()
