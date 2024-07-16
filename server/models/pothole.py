from pymongo import MongoClient


class Pothole:
    def __init__(self, lon, lat, number_of_pot_holes, identified_time):
        self.lon = lon
        self.lat = lat
        self.number_of_pot_holes = number_of_pot_holes
        self.identified_time = identified_time

    def to_dict(self):
        return {
            "lon": self.lon,
            "lat": self.lat,
            "number_of_pot_holes": self.number_of_pot_holes,
            "identified_time": self.identified_time,
        }

    def save_to_mongo(self, db_name, collection_name):
        client = MongoClient('localhost', 27017)
        db = client[db_name]
        collection = db[collection_name]
        collection.insert_one(self.to_dict())

    @staticmethod
    def get_all_locations(db_name, collection_name):
        client = MongoClient('localhost', 27017)
        db = client[db_name]
        collection = db[collection_name]
        return [location for location in collection.find()]
