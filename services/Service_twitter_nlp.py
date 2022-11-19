from flask_restx import Resource
from models.twitter_nlp_model import api, Twitter_Payload
from utilities.cache import cache
from bl.twitter_nlp import fetch_tweets_analysis
import json

@api.route('/analyse')
class Follow(Resource):
    @api.expect(Twitter_Payload)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        response = fetch_tweets_analysis(api.payload['keyword'], api.payload['number_of_tweets'])
        return response
