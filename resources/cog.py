from flask import request, jsonify
from flask_restx import Resource, Namespace, marshal_with, fields
from models.cog import Cog, db

api = Namespace('cog')


@api.route('/')
class CogListResource(Resource):
    def get(self):
        all_cogs = Cog.query.all()
        return all_cogs

    def post(self):
        name = request.json['name']
        description = request.json['description']

        new_cog = Cog(name, description)

        db.session.add(new_cog)
        db.session.commit()

        return new_cog


@api.route('/<int:id>')
class CogResource(Resource):
    def get(self, id):
        cog = Cog.query.get(id)
        return cog

    def put(self, id):
        cog = Cog.query.get(id)
        cog.name = request.json['name']
        cog.description = request.json['description']

        db.session.commit()

        return cog

    def delete(self, id):
        cog = Cog.query.get(id)

        db.session.delete(cog)
        db.session.commit()

        return True