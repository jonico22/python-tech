from flask_smorest import Blueprint
bp = Blueprint('categorias', __name__,description="Operations on Category")

from Category import routes
