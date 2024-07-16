from datetime import datetime

import requests
from bs4 import BeautifulSoup

from server.models.pothole import Pothole

ESP32_IP_ADDRESS = "http://192.168.1.100"


def get_location() -> (float, float):
    response = requests.get(ESP32_IP_ADDRESS)

    soup = BeautifulSoup(response.text, 'html.parser')

    lat = float(soup.find(id='lat').text)
    lon = float(soup.find(id='lon').text)

    return lon, lat


def identified_pothole(number_of_pot_holes):
    (lon, lat) = get_location()
    add_to_database(number_of_pot_holes, lon, lat)
    pass


def add_to_database(number_of_pot_holes, lon, lat):
    timestamp = datetime.now()
    new_pothole = Pothole(lon=lon, lat=lat, number_of_pot_holes=number_of_pot_holes,
                          identified_time=timestamp)
    new_pothole.save_to_mongo(db_name="pothole", collection_name="your_collection_name")
