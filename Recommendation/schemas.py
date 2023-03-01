from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class RecommendationSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'description','user_id', 'event_id', 'category_id', 'status')

class ParamsRecommendationSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=100))
    description = fields.Str(required=True, validate=Length(max=100))
    user_id = fields.Integer(required=True)
    event_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)

recommendation_schema = RecommendationSchema()
recommendations_schema = RecommendationSchema(many=True)
params_recommendations_schema = ParamsRecommendationSchema()
