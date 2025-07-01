import json
from config import config_helpers

def insert_projects_from_file(file_path="data/project.txt"):
    coll = config_helpers.get_mongo_collection()
    with open(file_path, 'r') as f:
        data = json.load(f)
    docs = data if isinstance(data, list) else [data]
    coll.delete_many({})
    coll.insert_many(docs)
    print(f"✅ Inserted {len(docs)} document(s) into MongoDB.")
