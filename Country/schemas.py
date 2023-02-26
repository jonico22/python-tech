from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class CountrySchema(Schema):
    class Meta:
        fields = ('id', 'name', 'code','status')

class ParamsCountrySchema(Schema):
    name = fields.Str(required=True, validate=Length(max=100))
    code = fields.Str(required=True, validate=Length(max=100))

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)
params_countries_schema = ParamsCountrySchema()
