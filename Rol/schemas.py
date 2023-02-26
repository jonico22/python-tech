from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class RolSchema(Schema):
    class Meta:
        fields = ('id', 'name','status')

class ParamsRolSchema(Schema):
    name = fields.Str(required=True, validate=Length(max=100))

rol_schema = RolSchema()
roles_schema = RolSchema(many=True)
params_roles_schema = ParamsRolSchema()