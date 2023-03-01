from flask_smorest import Blueprint
bp = Blueprint('recomendaciones', __name__,description="Operations on Recommendation ")

from Recommendation import routes
