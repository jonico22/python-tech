from models import db
from sqlalchemy import desc, asc

class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    name = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=True,default=db.func.current_timestamp())
    status =  db.Column(db.Boolean, nullable=True,default=1)
    user = db.relationship(
        "User",
        backref="roles",
        cascade="delete,merge"
    )
    @classmethod
    def new(cls, name):
        return Rol(name=name)

    @classmethod
    def get_by_page(cls, order, page, per_page=10):
        sort = desc(Rol.id) if order == 'desc' else asc(Rol.id)
        return Rol.query.order_by(sort).paginate(page=page, per_page=per_page).items

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
        