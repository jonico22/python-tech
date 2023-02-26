from flask import Blueprint
bp = Blueprint('paises', __name__)

from Country import routes
