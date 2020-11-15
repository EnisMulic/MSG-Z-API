from pymongo import errors
from .context import db

class CogRepository:
    def __init__(self):
        self.dbSet = db.configs

    def get_all(self):
        return [doc for doc in self.dbSet.find()]

    def get(self, name: str):
        return self.dbSet.find_one({"name": name})

    def create(self, config):
        result = self.dbSet.insert_one(config)
        if result.acknowledged == True:
            return config
        return None

    def update(self, name, config):
        result = self.dbSet.update_one({"name": name}, {"$set": config})
        if result.modified_count == 1:
            return config
        return None

    def delete(self, name):
        result = self.dbSet.delete_one({"name": name})
        return result.deleted_count != 0