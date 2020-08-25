from flask import Blueprint
from flask_restful import Api

from resources.cog import CogResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(CogResource, '/cog')



# Run Server
if __name__ == '__main__':
    from imports import db

    db.init_app(app)
    app.run(debug=True)