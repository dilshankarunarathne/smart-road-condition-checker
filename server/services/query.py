from server.models.pothole import Pothole


def query_all_locations():
    all_locations = Pothole.get_all_locations(db_name="pothole", collection_name="data")
