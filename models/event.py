from models import db
from sqlalchemy import desc, asc
from sqlalchemy.schema import ForeignKey

class Event(db.Model):
    __tablename__ = 'eventos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    title = db.Column(db.String(), nullable=False,unique=True)
    address = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    date_event = db.Column(db.DateTime(), nullable=False)
    image = db.Column(db.String())
    url = db.Column(db.String())
    user_id = db.Column(db.Integer,ForeignKey("users.id",ondelete="CASCADE"))
    country_id = db.Column(db.Integer,ForeignKey("paises.id",ondelete="CASCADE"))
    created_at = db.Column(db.DateTime(), nullable=False,default=db.func.current_timestamp())
    status =  db.Column(db.Boolean, nullable=False,default=1)
    recommendation = db.relationship(
            "Recommendation",
            backref="eventos",
            cascade="delete,merge"
    ) 
    
    
    @classmethod
    def new(cls, title, address, description, date_event, image, url, user_id, country_id):
        return Event(title=title, address=address, description=description, date_event=date_event, image=image, url=url, user_id=user_id, country_id=country_id)

    @classmethod
    def get_by_page(cls, order, page, per_page=10):
        sort = desc(Event.id) if order == 'desc' else asc(Event.id)
        return Event.query.order_by(sort).paginate(page=page, per_page=per_page).items

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