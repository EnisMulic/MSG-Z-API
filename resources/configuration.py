from flask import request, jsonify
from flask_restx import Resource, Namespace
from models.configuration import Configuration


api = Namespace('configuration')


@api.route("/")
class ConfigurationListResource(Resource):
    def get(self):
        all_configurations = Configuration.query.all()
        result = configurations_schema.dump(all_configurations)
        return jsonify(result)

    def post(self):
        configuration.key = request.json['key']
        configuration.value = request.json['value']
        configuration.cog_id = request.json['cog_id']

        new_configuration = Configuration(key, value, cog_id)

        db.session.add(new_cog)
        db.session.commit()

        return cog_schema.jsonify(new_configuration)

@api.route("/<int:id>")
class ConfigurationResource(Resource):
    def get(self, id):
        configuration = Configuration.query.get(id)
        result = configuration_schema.dump(configuration)
        return jsonify(result)

    def put(self, id):
        configuration = Configuration.query.get(id)
        configuration.key = request.json['key']
        configuration.value = request.json['value']
        configuration.cog_id = request.json['cog_id']

        db.session.commit()

        return cog_schema.jsonify(configuration)

    def delete(self, id):
        configuration = Configuration.query.get(id)

        db.session.delete(configuration)
        db.session.commit()

        return True