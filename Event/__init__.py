from flask_smorest import Blueprint
bp = Blueprint('eventos', __name__,description="Operations on Events")

from Event import routes
