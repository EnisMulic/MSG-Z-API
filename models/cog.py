from . import ma
from database import db

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
  class Meta:
    fields = ('id', 'name', 'description')

# Init schema
cog_schema = CogSchema()
cogs_schema = CogSchema(many = True)