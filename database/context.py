from pymongo import MongoClient
import pymongo

client = MongoClient("mongodb://mongo:27017/")
db = client.msg_z_config
db.configs.create_index([('name', pymongo.ASCENDING)], unique=True)