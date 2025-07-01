from config import config_helpers

def fetch_projects_from_mongo(query=None):
    coll = config_helpers.get_mongo_collection()
    return list(coll.find(query or {}))
