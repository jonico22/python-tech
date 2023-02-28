from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'username','email','password','rol_id','status')

class ParamsUserSchema(Schema):
    username = fields.Str(required=True, validate=Length(max=100))
    email = fields.Str(required=True,validate=Length(max=100))
    password = fields.Str(required=True, validate=Length(max=100))
    rol_id = fields.Int(required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
params_users_schema = ParamsUserSchema()