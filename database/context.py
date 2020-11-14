from pymongo import MongoClient
import pymongo

client = MongoClient("mongodb://localhost:27017/msg_z_config")

client.msg_z_config.configs.create_index([('name', pymongo.ASCENDING)], unique=True)