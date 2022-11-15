from flask_restx import Resource
from models.user_mapping_model import api, follow_payload_model, followers_by_id
from dal.users_details import FollowUser, GetAllFollowersById, GetAllFollowersMapping, GetAllUser, UnFollowUser
from utilities.cache import cache


@api.route('/follow')
class Follow(Resource):
    @api.expect(follow_payload_model)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        response = FollowUser((api.payload['followed_by'], api.payload['follows']))
        return response
 

@api.route('/Unfollow')
class Unfollow(Resource):
    @api.expect(follow_payload_model)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        response = UnFollowUser((api.payload['followed_by'], api.payload['follows']))
        if response in [0,1]:
            return 'Success'
        else:
            return 'Failed'


@api.route('/GetAllFollowDetails')
class GetAllFollowDetails(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def get(self):
        response = GetAllFollowersMapping()
        return response

@api.route('/GetFollowerdListById')
class GetFollowerdListById(Resource):
    @api.expect(followers_by_id)
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def post(self):
        response = GetAllFollowersById((api.payload['follows']))
        return response
        

@api.route('/GetAllUserDetails')
class GetAllUserDetails(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def get(self):
        response = GetAllUser()
        return response


@cache.cached(timeout=3600)
def testing(i):
    print('w/o cach')
    return i


@api.route('/test')
class test(Resource):
    @api.doc(response={200: 'Success', 400: 'Validation Error'})
    @api.doc(security='apikey')
    @api.response('default', 'Error')
    def get(self):
        for i in range(10):
            print(f'calling cache for {i}th time')
            testing(i)
        return 1