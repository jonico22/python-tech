from flask import request
from Event import bp
from models import Event

from util import response
from util import not_found
from util import bad_request
from util import validate_auth

from .schemas import event_schema
from .schemas import events_schema
from .schemas import params_events_schema
from flask_jwt_extended import jwt_required

def set_Event(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        event = Event.query.filter_by(id=id).first()
        if event is None:
            return not_found()
        return function(event)
    wrap.__name__ = function.__name__
    return wrap

#INICIAR GET
@bp.route('/', methods=['GET'])
def get_Events():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'desc')
    Events = Event.get_by_page(order, page)
    return response(events_schema.dump(Events))

#INICIAR DETALLE ID
@bp.route('/<id>', methods=['GET'])
@set_Event
def get_Event(event):
    return response(event_schema.dump(event))

#INICIAR GUARDAR
@bp.route('/', methods=['POST'])
@jwt_required()
def create_event():
    json = request.get_json(force=True)
    error = params_events_schema.validate(json)
    if error:
        print(error)
        return bad_request()
    event = Event.new(json['title'], json['address'], json['description'], json['date_event'], json['image'], json['url'], json['user_id'], json['country_id']) 
    if event.save():
        return response(event_schema.dump(event))
    
    return bad_request()

#INICIAR ACTUALIZAR
@bp.route('/<id>', methods=['PUT'])
@jwt_required()
@set_Event
def update_Event(event):
    json = request.get_json(force=True)
    event.title = json.get('title', event.title)
    event.address = json.get('address', event.address)
    event.description = json.get('description', event.description)
    event.date_event = json.get('date_event', event.date_event)
    event.image = json.get('image', event.image)
    event.url = json.get('url', event.url)   
    event.user_id = json.get('user_id', event.user_id)  
    event.country_id = json.get('country_id', event.country_id)   
    if event.save():
        return response(event_schema.dump(event))

    return bad_request()

#INICIAR ELIMINAR
@bp.route('/<id>', methods=['DELETE'])
@jwt_required()
@set_Event
def delete_Event(event):
    if event.delete():
        return response(event_schema.dump(event))
    return bad_request()
