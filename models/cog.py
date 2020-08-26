from flask import Flask
from database import db


class Cog(db.Model):
  __tablename__ = 'cogs'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  

  def __init__(self, name, description):
    self.name = name
    self.description = description
