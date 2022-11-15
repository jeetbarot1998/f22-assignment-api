from flask_restx import Namespace, reqparse, fields, inputs

api = Namespace('TwitterNLP', description='Twitter NLP')

Twitter_Payload = api.model(
    'Twitter_Payload', {
        'keyword' : fields.String(attribute='keyword')
    }
)