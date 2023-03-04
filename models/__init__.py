from flask_sqlalchemy import SQLAlchemy

# session_options={"expire_on_commit": False} =>
# would allow to manipulate out of date models
# after a transaction has been committed
# ! be aware that the above can have unintended side effects
db = SQLAlchemy()

from models.rol import Rol
from models.user import User
from models.category import Category
from models.country import Country
from models.event import Event
from models.recomendation import Recommendation                  

      
