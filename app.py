from flask import Blueprint
from flask_restx import Api

from resources.cog import api as cog_api
from resources.configuration import api as configuration_api


api_bp = Blueprint('api', __name__)
api = Api(
    api_bp, 
    version = '1.0', 
    title = 'MSG-Z API',
    description = 'A simple API for configuration of MSG-Z'
)

api.add_namespace(cog_api)
api.add_namespace(configuration_api)

# ns = api.namespace('todos', description='TODO operations')
# ns.add_resource(CogListResource, '/cog')
# ns.add_resource(CogResource, '/cog/<int:id>')

# Route
# api.add_resource(CogListResource, '/cog')
# api.add_resource(CogResource, '/cog/<int:id>')
# api.add_resource(ConfigurationListResource, '/configuration')



# Run Server
if __name__ == '__main__':
    from imports import db

    db.init_app(app)
    app.run(debug=True)