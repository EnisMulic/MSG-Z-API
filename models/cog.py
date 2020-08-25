from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from imports import db, ma


# Cog Model
class Cog(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  

  def __init__(self, name, description):
    self.name = name
    self.description = description


# Cog Schema
class CogSchema(ma.Schema):
  id = fields.Integer()
  name = fields.String(required=True)
  description = fields.String()