from server.models.pothole import Pothole

all_locations = Pothole.get_all_locations(db_name="pothole", collection_name="your_collection_name")
for location in all_locations:
    print(location)
