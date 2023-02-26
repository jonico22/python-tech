from flask_smorest import Blueprint
bp = Blueprint('paises', __name__)

from Country import routes
