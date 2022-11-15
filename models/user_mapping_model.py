from flask_restx import Namespace, reqparse, fields, inputs

api = Namespace('UserMapping', description='User mapping')


follow_payload_model = api.model(
    'follow_payload_model', {
        'followed_by' : fields.Integer(attribute='followed_by'),
        'follows' : fields.Integer(attribute='follows')
    }
)

followers_by_id = api.model(
    'followers_by_id', {
        'follows' : fields.Integer(attribute='follows')
    }
)