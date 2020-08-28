from flask import request
from flask_restx import Resource, Namespace, fields, marshal_with

from models.configuration import Configuration, db, ConfigurationSchema
from requests.configuration_request import ConfigurationUpsertRequest

ns = Namespace('configuration')

model = ns.model('Configuration', {
    "id": fields.Integer(required = True),
    "key": fields.String(required = True),
    "value": fields.String(required = True),
    "cog_id": fields.Integer(required = True)
})


configurationUpsertRequest = ns.model('ConfigurationUpsertRequest', ConfigurationUpsertRequest)


configuration_schema = ConfigurationSchema()
configurations_schema = ConfigurationSchema(many = True)


@ns.route("/")
class ConfigurationListResource(Resource):
    def get(self):
        entitys = Configuration.query.all()
        return configurations_schema.dump(entitys)

    @ns.doc(body = configurationUpsertRequest)
    def post(self):
        entity = configuration_schema.load(request.json)

        db.session.add(entity)
        db.session.commit()

        return configuration_schema.dump(entity)

@ns.route("/<int:id>")
class ConfigurationResource(Resource):
    def get(self, id):
        entity = Configuration.query.get(id)
        return configuration_schema.dump(entity)

    @ns.doc(body = configurationUpsertRequest)
    def put(self, id):
        configuration = configuration_schema.load(request.json, instance = Configuration.query.get(id), partial = True)

        db.session.commit()

        return configuration_schema.dump(configuration)

    def delete(self, id):
        entity = Configuration.query.get(id)

        db.session.delete(entity)
        db.session.commit()

        return True