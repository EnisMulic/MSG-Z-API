from pymongo import errors
from .context import client

def get_all():
    return [doc for doc in client.msg_z_config.configs.find()]

def get(name: str):
    return client.msg_z_config.configs.find_one({"name": name})

def create(config):
    result = client.msg_z_config.configs.insert_one(config)
    if result.acknowledged == True:
        return config
    return None

def update(name, config):
    result = client.msg_z_config.configs.update_one({"name": name}, {"$set": config})
    if result.modified_count == 1:
        return config
    return None

def delete(name):
    result = client.msg_z_config.configs.delete_one({"name": name})
    return result.deleted_count != 0