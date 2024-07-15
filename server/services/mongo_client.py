from pymongo import MongoClient

from server.config import config


def get(section: str, key: str):
    if section == 'database' and key == 'cluster':
        return MongoClient('mongodb://localhost:27017/')['pothole']
    else:
        return config[section][key]
