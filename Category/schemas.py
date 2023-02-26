from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class CategorySchema(Schema):
    class Meta:
        fields = ('id', 'name','status')

class ParamsCategorySchema(Schema):
    name = fields.Str(required=True, validate=Length(max=100))

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
params_categories_schema = ParamsCategorySchema()
