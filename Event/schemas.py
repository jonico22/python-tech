from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class EventSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'address','description', 'date_event', 'image', 'url', 'user_id', 'country_id', 'status')

class ParamsEventSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=100))
    address = fields.Str(required=True, validate=Length(max=100))
    description = fields.Str(required=True)
    date_event = fields.DateTime(required=True)
    image = fields.Str(validate=Length(max=100))
    url = fields.Str(validate=Length(max=100))
    user_id = fields.Integer(required=True)
    country_id = fields.Integer(required=True)

event_schema = EventSchema()
events_schema = EventSchema(many=True)
params_events_schema = ParamsEventSchema()
