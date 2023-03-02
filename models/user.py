from models import db
from sqlalchemy.schema import ForeignKey
from sqlalchemy import desc, asc
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    username = db.Column(db.String(), nullable=False,unique=True)
    email = db.Column(db.String(), nullable=False,unique=True)
    password = db.Column(db.String(), nullable=False)
    rol_id = db.Column(db.Integer,ForeignKey("roles.id",ondelete="CASCADE"))
    created_at = db.Column(db.DateTime(), nullable=False,default=db.func.current_timestamp())
    status =  db.Column(db.Boolean, nullable=False,default=1)
    event = db.relationship(
        "Event",
        backref="users",
        cascade="delete,merge"
    )
    recommendation = db.relationship(
            "Recommendation",
            backref="users",
            cascade="delete,merge"
    ) 

    def set_password(self, password):
        self.password = generate_password_hash(password,method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()
    
    @classmethod
    def new(cls, username,email,password,rol_id):
        return User(username=username,email=email,password=password,rol_id=rol_id)

    @classmethod
    def get_by_page(cls, order, page, per_page=10):
        sort = desc(User.id) if order == 'desc' else asc(User.id)
        return User.query.order_by(sort).paginate(page=page, per_page=per_page).items

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