from flask import Blueprint
bp = Blueprint('eventos', __name__)

from Event import routes
