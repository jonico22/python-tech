from flask_sqlalchemy import SQLAlchemy

# session_options={"expire_on_commit": False} =>
# would allow to manipulate out of date models
# after a transaction has been committed
# ! be aware that the above can have unintended side effects
db = SQLAlchemy()
from sqlalchemy.schema import ForeignKey
from sqlalchemy import desc, asc
from sqlalchemy.event import listen
from werkzeug.security import generate_password_hash, check_password_hash

class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    name = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False,default=db.func.current_timestamp())
    status =  db.Column(db.Boolean, nullable=False,default=1)
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
        
def insert_roles(*args, **kwargs):
    db.session.add( Rol(name='Admin'))
    db.session.add( Rol(name='Colaborador'))
    db.session.add( Rol(name='Organizador'))
    db.session.commit()

listen(Rol.__table__, 'after_create', insert_roles)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    username = db.Column(db.String(), nullable=False,unique=True)
    email = db.Column(db.String(), nullable=False,unique=True)
    password = db.Column(db.String(), nullable=False)
    rol_id = db.Column(db.Integer,ForeignKey("roles.id",ondelete="CASCADE"))
    created_at = db.Column(db.DateTime(), nullable=False,default=db.func.current_timestamp())
    status =  db.Column(db.Boolean, nullable=False,default=1)

    def set_password(self, password):
        self.password = generate_password_hash(password)

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

class Category(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    name = db.Column(db.String(), nullable=False,unique=True)
    created_at = db.Column(db.DateTime(), nullable=False,default=db.func.current_timestamp())
    status =  db.Column(db.Boolean, nullable=False,default=1)
    
    @classmethod
    def new(cls, name):
        return Category(name=name)

    @classmethod
    def get_by_page(cls, order, page, per_page=10):
        sort = desc(Category.id) if order == 'desc' else asc(Category.id)
        return Category.query.order_by(sort).paginate(page=page, per_page=per_page).items

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

class Country(db.Model):
    __tablename__ = 'paises'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    name = db.Column(db.String(), nullable=False,unique=True)
    code = db.Column(db.String(), nullable=False,unique=True)
    created_at = db.Column(db.DateTime(), nullable=False,default=db.func.current_timestamp())
    status =  db.Column(db.Boolean, nullable=False,default=1)
    
    @classmethod
    def new(cls, name, code):
        return Country(name=name, code=code)

    @classmethod
    def get_by_page(cls, order, page, per_page=10):
        sort = desc(Country.id) if order == 'desc' else asc(Country.id)
        return Country.query.order_by(sort).paginate(page=page, per_page=per_page).items

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
