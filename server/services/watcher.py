from datetime import datetime

from server.models.pothole import Pothole


def get_location() -> (float, float):
    pass


def identified_pothole(number_of_pot_holes):
    (lon, lat) = get_location()
    add_to_database(number_of_pot_holes, lon, lat)
    pass


def add_to_database(number_of_pot_holes, lon, lat):
    timestamp = datetime.now()
    new_pothole = Pothole(_id="new_id", lon=123.456, lat=78.910, number_of_pot_holes=2, identified_time=timestamp)
    new_pothole.save_to_mongo(db_name="your_db_name", collection_name="your_collection_name")
