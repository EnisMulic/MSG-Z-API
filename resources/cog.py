from flask import request, jsonify
from flask_restx import Resource, Namespace, marshal_with, fields


from requests.cog_request import CogUpsertRequest
from database import cog as cog_repo

from bson import json_util
import json


ns = Namespace('cog')

cogUpsertRequest = ns.model('CogUpsertRequest', CogUpsertRequest)



@ns.route('/')
class CogListResource(Resource):
    def get(self):
        entitys = cog_repo.get_all()
        result = json.loads(json_util.dumps(entitys))
        return result

    @ns.doc(body = cogUpsertRequest)
    def post(self):
        entity = cog_repo.create(request.json)
        
        return json.loads(str(entity))


@ns.route('/<name>')
class CogResource(Resource):
    def get(self, name):
        entity = cog_repo.get(name)
        return json.loads(json_util.dumps(entity))

    @ns.doc(body = cogUpsertRequest)
    def put(self, name):
        entity = cog_repo.update(name)

        return json.loads(json_util.dumps(entity))
    
    @ns.response(200, "Success")
    @ns.response(204, "No Content")
    def delete(self, name):
        entity = cog_repo.delete(name)

        if entity != None:
            return {"status": "success"}, 200
        return {"status": "no content"}, 204
        
