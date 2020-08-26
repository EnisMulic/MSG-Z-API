from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from imports import db, ma


# Cog Model
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


# Cog Schema
class ConfigurationSchema(ma.Schema):
  id = fields.Integer(dump_only = True)
  key = fields.String(required = True)
  value = fields.String(required = True)
  cog_id = fields.Integer(required = True)