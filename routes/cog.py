
from models import cog_schema, cogs_schema
from flask_restful import Resource, reqparse

class CogList(Resource):
    def get(self):
        all_cogs = cog.query.all()
        result = cogs_schema.dump(all_cogs)
        return jsonify(result) 


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