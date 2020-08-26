from flask import request, jsonify
from flask_restx import Resource, Namespace, marshal
from models.cog import Cog, CogSchema, db

api = Namespace('cog')

cogs_schema = CogSchema(many = True)
cog_schema = CogSchema()


@api.route('/')
class CogListResource(Resource):
    def get(self):
        all_cogs = Cog.query.all()
        result = cogs_schema.dump(all_cogs)
        return result


    def post(self):
        name = request.json['name']
        description = request.json['description']

        new_cog = Cog(name, description)

        db.session.add(new_cog)
        db.session.commit()

        return cog_schema.jsonify(new_cog)


@api.route('/<int:id>')
class CogResource(Resource):
    def get(self, id):
        cog = Cog.query.get(id)
        result = cog_schema.dump(cog)
        return jsonify(result) 

    def put(self, id):
        cog = Cog.query.get(id)
        cog.name = request.json['name']
        cog.description = request.json['description']

        db.session.commit()

        return cog_schema.jsonify(cog)

    def delete(self, id):
        cog = Cog.query.get(id)

        db.session.delete(cog)
        db.session.commit()

        return True