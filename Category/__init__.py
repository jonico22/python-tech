from flask_smorest import Blueprint
bp = Blueprint('categorias', __name__)

from Category import routes
