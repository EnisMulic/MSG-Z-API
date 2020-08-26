from flask import request
from flask_restx import Resource, Namespace, fields, marshal_with
from models.configuration import Configuration


api = Namespace('configuration')

model = api.model('Configuration', {
    "id": fields.Integer(required = True),
    "key": fields.String(required = True),
    "value": fields.String(required = True),
    "cog_id": fields.Integer(required = True)
})


@api.route("/")
class ConfigurationListResource(Resource):
    @api.marshal_with(model)
    def get(self):
        all_configurations = Configuration.query.all()
        return all_configurations

    @api.marshal_with(model)
    def post(self):
        configuration.key = request.json['key']
        configuration.value = request.json['value']
        configuration.cog_id = request.json['cog_id']

        new_configuration = Configuration(key, value, cog_id)

        db.session.add(new_cog)
        db.session.commit()

        return new_configuration

@api.route("/<int:id>")
class ConfigurationResource(Resource):
    @api.marshal_with(model)
    def get(self, id):
        configuration = Configuration.query.get(id)
        return configuration

    @api.marshal_with(model)
    def put(self, id):
        configuration = Configuration.query.get(id)
        configuration.key = request.json['key']
        configuration.value = request.json['value']
        configuration.cog_id = request.json['cog_id']

        db.session.commit()

        return configuration

    def delete(self, id):
        configuration = Configuration.query.get(id)

        db.session.delete(configuration)
        db.session.commit()

        return True