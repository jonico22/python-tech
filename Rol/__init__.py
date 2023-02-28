from flask_smorest import Blueprint
bp = Blueprint('roles', __name__ ,description="Operations on Roles")

from Rol import routes