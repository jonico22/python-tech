from flask_smorest import Blueprint
bp = Blueprint('paises', __name__,description="Operations on Country")

from Country import routes
