from flask import Flask
from database import db

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Configuration(db.Model):
  __tablename__ = 'configurations'

  id = db.Column(db.Integer, primary_key = True)
  key = db.Column(db.String(100), nullable = False)
  value = db.Column(db.String(100), nullable = False)

  cog_id = db.Column(db.Integer, db.ForeignKey('cogs.id', ondelete = 'CASCADE'), nullable = False)
  cog = db.relationship('Cog', backref = db.backref('configurations'))
  

  def __init__(self, key, value, cog_id):
    self.key = key
    self.value = value
    self.cog_id = cog_id

class ConfigurationSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Configuration
    load_instance = True
    transient = True