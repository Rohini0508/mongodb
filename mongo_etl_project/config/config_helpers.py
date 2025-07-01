import yaml
from pymongo import MongoClient
import mysql.connector
import pyodbc  # install with: pip install pyodbc

def load_config(path='config/db_config1.yaml'):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def get_mongo_collection():
    cfg = load_config()
    uri = cfg['mongodb']['uri']
    dbname = cfg['mongodb']['database']
    coll = cfg['mongodb']['collection']
    client = MongoClient(uri)
    return client[dbname][coll]

def get_mysql_connection():
    cfg = load_config()
    m = cfg['mysql']
    return mysql.connector.connect(
        host=m['host'], user=m['user'], password=m['password'], database=m['database']
    )

def get_sqlserver_connection():
    cfg = load_config()
    s = cfg['sqlserver']
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={s['server']};DATABASE={s['database']};UID={s['user']};PWD={s['password']}"
    )
    return pyodbc.connect(conn_str)
