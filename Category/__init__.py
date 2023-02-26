from flask import Blueprint
bp = Blueprint('categorias', __name__)

from Category import routes
