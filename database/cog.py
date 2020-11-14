from .context import client

def get_all():
    return [doc for doc in client.msg_z_config.configs.find()]

def get(name: str):
    return client.msg_z_config.configs.find_one({"name": name})

def create(config):
    return client.msg_z_config.configs.insert_one(config)

def update(name):
    pass

def delete(name):
    pass
