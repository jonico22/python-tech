from flask import jsonify

def bad_request():
  return jsonify({
    'success': False,
    'data': [],
    'messages': 'Petición incorrecta',
    'code': 400
  }), 400

def validate_auth(msg):
  return jsonify({
    'success': False,
    'data': [],
    'messages': msg,
    'code': 401
  }), 401

def not_found():
  return jsonify(
    {
      'success': False,
      'data': [],
      'message': 'Ruta no encontrada',
      'code': 404
    }
  ), 404

def response(data):
    return jsonify(
      {
        'success': True,
        'data': data,
        'message': '',
        'code': 200
      }  
    ), 200