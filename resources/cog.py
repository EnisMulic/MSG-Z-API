from flask import request, jsonify
from flask_restx import Resource, Namespace
from models.cog import Cog, CogSchema, db

api = Namespace('cog')

cogs_schema = CogSchema(many = True)
cog_schema = CogSchema()

@api.route('/')
class CogList(Resource):
    def get(self):
        all_cogs = Cog.query.all()
        result = cogs_schema.dump(all_cogs)
        return jsonify(result) 


    def post(self):
        name = request.json['name']
        description = request.json['description']

        new_cog = Cog(name, description)

        db.session.add(new_cog)
        db.session.commit()

        return cog_schema.jsonify(new_cog)


@api.route('/<int:id>')
class Cog(Resource):
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


    




# # Create a cog
# @cog.route('/cog', methods=['POST'])
# def add_cog():
#   name = request.json['name']
#   description = request.json['description']

#   new_cog = cog(name, description)

#   db.session.add(new_cog)
#   db.session.commit()

#   return cog_schema.jsonify(new_cog)

# # Get All cogs
# @cog.route('/cog', methods=['GET'])
# def get_cogs():
#   all_cogs = cog.query.all()
#   result = cogs_schema.dump(all_cogs)
#   return jsonify(result)

# # Get Single cogs
# @cog.route('/cog/<id>', methods=['GET'])
# def get_cog(id):
#   cog = cog.query.get(id)
#   return cog_schema.jsonify(cog)

# # Update a cog
# @cog.route('/cog/<id>', methods=['PUT'])
# def update_cog(id):
#   cog = cog.query.get(id)

#   cog.name = request.json['name']
#   cog.description = request.json['description']

#   db.session.commit()

#   return cog_schema.jsonify(cog)

# # Delete cog
# @cog.route('/cog/<id>', methods=['DELETE'])
# def delete_cog(id):
#   cog = cog.query.get(id)
#   db.session.delete(cog)
#   db.session.commit()

#   return cog_schema.jsonify(cog)