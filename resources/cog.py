from flask import request
from flask_restx import Resource, Namespace, marshal_with, fields
from models.cog import Cog, db

api = Namespace('cog')

model = api.model('Cog', {
    "id": fields.Integer(required = True),
    "name": fields.String(required = True),
    "description": fields.String(required = True),
})


@api.route('/')
class CogListResource(Resource):
    @api.marshal_with(model)
    def get(self):
        all_cogs = Cog.query.all()
        return all_cogs

    @api.marshal_with(model)
    def post(self):
        name = request.json['name']
        description = request.json['description']

        new_cog = Cog(name, description)

        db.session.add(new_cog)
        db.session.commit()

        return new_cog


@api.route('/<int:id>')
class CogResource(Resource):
    @api.marshal_with(model)
    def get(self, id):
        cog = Cog.query.get(id)
        return cog

    @api.marshal_with(model)
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