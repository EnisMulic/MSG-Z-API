from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restful import reqparse, Api, Resource 
import os


from routes.cog import CogList

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(CogList, '/cog')


# Run Server
if __name__ == '__main__':
    from database import db

    db.init_app(app)
    app.run(debug=True)