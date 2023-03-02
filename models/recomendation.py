from models import db
from sqlalchemy import desc, asc
from sqlalchemy.schema import ForeignKey

class Recommendation(db.Model):
    __tablename__ = 'recomendaciones'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    title = db.Column(db.String(), nullable=False,unique=True)
    description = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer,ForeignKey("users.id",ondelete="CASCADE"))
    event_id = db.Column(db.Integer,ForeignKey("eventos.id",ondelete="CASCADE"))
    category_id = db.Column(db.Integer,ForeignKey("categorias.id",ondelete="CASCADE"))
    created_at = db.Column(db.DateTime(), nullable=False,default=db.func.current_timestamp())
    status =  db.Column(db.Boolean, nullable=False,default=1)
    
    @classmethod
    def new(cls, title, description, user_id, event_id, category_id):
        return Recommendation(title=title, description=description, user_id=user_id, event_id=event_id, category_id=category_id)

    @classmethod
    def get_by_page(cls, order, page, per_page=10):
        sort = desc(Recommendation.id) if order == 'desc' else asc(Recommendation.id)
        return Recommendation.query.order_by(sort).paginate(page=page, per_page=per_page).items

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False        