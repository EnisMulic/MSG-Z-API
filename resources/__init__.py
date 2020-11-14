from flask import Blueprint
from flask_restx import Api

from .cog import ns as cog_ns

api_bp = Blueprint('api', __name__)
api = Api(
    api_bp,
    version = '1.0', 
    title = 'MSG-Z API',
    description = 'A simple API for configuration of MSG-Z'
)

api.add_namespace(cog_ns)