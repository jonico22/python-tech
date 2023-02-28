from flask_smorest import Blueprint
bp = Blueprint('auth', __name__,description="Operations on Auth")

from auth import routes