from flask_smorest import Blueprint
bp = Blueprint('user', __name__,description="Operations on Users")

from User import routes