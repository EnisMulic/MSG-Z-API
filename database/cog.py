from pymongo import errors
from .context import db

def get_all():
    return [doc for doc in db.configs.find()]

def get(name: str):
    return db.configs.find_one({"name": name})

def create(config):
    result = db.configs.insert_one(config)
    if result.acknowledged == True:
        return config
    return None

def update(name, config):
    result = db.configs.update_one({"name": name}, {"$set": config})
    if result.modified_count == 1:
        return config
    return None

def delete(name):
    result = db.configs.delete_one({"name": name})
    return result.deleted_count != 0