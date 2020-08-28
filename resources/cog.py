from flask import request
from flask_restx import Resource, Namespace, marshal_with, fields

from models.cog import Cog, db, CogSchema
from models.configuration import Configuration
from .configuration import model as configModel

from requests.cog_request import CogUpsertRequest


ns = Namespace('cog')

# model = ns.model('Cog', {
#     "id": fields.Integer(required = True),
#     "name": fields.String(required = True),
#     "description": fields.String(required = True),
# })

cogUpsertRequest = ns.model('CogUpsertRequest', CogUpsertRequest)

cog_schema = CogSchema()
cogs_schema = CogSchema(many = True)


@ns.route('/')
class CogListResource(Resource):
    def get(self):
        entitys = Cog.query.all()
        result = cogs_schema.dump(entitys)
        return result

    @ns.doc(body = cogUpsertRequest)
    def post(self):
        entity = cog_schema.load(request.json)

        db.session.add(entity)
        db.session.commit()

        return cog_schema.dump(entity)


@ns.route('/<int:id>')
class CogResource(Resource):
    def get(self, id):
        entity = Cog.query.get(id)
        return cog_schema.dump(entity)

    @ns.doc(body = cogUpsertRequest)
    def put(self, id):
        cog = cog_schema.load(request.json, instance = Cog.query.get(id), partial = True)

        db.session.commit()

        return cog_schema.dump(cog)

    def delete(self, id):
        entity = Cog.query.get(id)

        db.session.delete(entity)
        db.session.commit()

        return True


@ns.route('/<int:id>/configuration')
class CogConfigurationResource(Resource):
    @ns.marshal_with(configModel)
    def get(self, id):
        configuration = db.session.query(Configuration).filter(Configuration.cog_id == id).all()
        return configuration
