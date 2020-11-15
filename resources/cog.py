from flask import request
from flask_restx import Resource, Namespace, fields

from database import cog as cog_repo

from bson import json_util
import json

from pymongo import errors


ns = Namespace('cog')

cogUpsertRequest = ns.model('CogUpsertRequest', {
    "name": fields.String(required = True)
})



@ns.route('/')
class CogListResource(Resource):
    @ns.response(200, "Success")
    def get(self):
        entitys = cog_repo.get_all()
        result = json.loads(json_util.dumps(entitys))
        return result

    @ns.doc(body = cogUpsertRequest)
    @ns.response(200, "Success")
    @ns.response(409, "Conflict")
    def post(self):
        try:
            entity = cog_repo.create(request.json)
            
            return json.loads(json_util.dumps(entity))
        except errors.DuplicateKeyError as err:
            return {
                "status": "conflict",
                "errors": str(err.details)
            }, 409


@ns.route('/<name>')
class CogResource(Resource):
    @ns.response(200, "Success")
    def get(self, name):
        entity = cog_repo.get(name)
        return json.loads(json_util.dumps(entity))

    @ns.doc(body = cogUpsertRequest)
    @ns.response(200, "Success")
    @ns.response(404, "Not Found")
    def put(self, name):
        entity = cog_repo.update(name, request.json)
        
        if entity != None:
            return json.loads(json_util.dumps(entity))
        return {"status": "not found"}, 404
    
    @ns.response(200, "Success")
    @ns.response(204, "No Content")
    def delete(self, name):
        result = cog_repo.delete(name)

        if result == True:
            return {"status": "success"}, 200
        return {"status": "no content"}, 204
        
