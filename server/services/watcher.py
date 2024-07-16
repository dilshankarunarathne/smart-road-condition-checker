from datetime import datetime

from server.models.pothole import Pothole

import requests
from bs4 import BeautifulSoup


def get_location() -> (float, float):
    ESP32_IP_ADDRESS = "http://192.168.1.100"

    response = requests.get(ESP32_IP_ADDRESS)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the latitude and longitude from the HTML
    # This assumes that the latitude and longitude are contained in elements with ids 'lat' and 'lon' respectively
    lat = float(soup.find(id='lat').text)
    lon = float(soup.find(id='lon').text)

    return (lon, lat)


def identified_pothole(number_of_pot_holes):
    (lon, lat) = get_location()
    add_to_database(number_of_pot_holes, lon, lat)
    pass


def add_to_database(number_of_pot_holes, lon, lat):
    timestamp = datetime.now()
    new_pothole = Pothole(lon=lon, lat=lat, number_of_pot_holes=number_of_pot_holes,
                          identified_time=timestamp)
    new_pothole.save_to_mongo(db_name="pothole", collection_name="your_collection_name")
