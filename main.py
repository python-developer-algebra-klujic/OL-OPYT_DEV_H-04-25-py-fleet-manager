'''
- ispis svih vozila
- ispis detalja jednog vozila
- dodavanje novog vozila
'''
import json
from typing import Dict, List


FILE_PATH = 'sample_data/trucks_sample_eu.json'



def load_from_json() -> List:
    try:
        with open(FILE_PATH, 'r') as file_reader:
            return json.load(file_reader)

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')
        return []


def display_vehicle_data(vehicle: Dict) -> None:
    print()
    print(vehicle["id"])
    print(vehicle["vin"])
    print(vehicle["make"])
    print(vehicle["model"])
    print(vehicle["year"])
    print(vehicle["type"])
    print(vehicle["axle_config"])
    print(vehicle["euro_standard"])
    print(vehicle["engine_power_kw"])
    print(vehicle["fuel"])
    print(vehicle["gvw_kg"])
    print(vehicle["payload_kg"])
    print(vehicle["length_m"])
    print(vehicle["width_m"])
    print(vehicle["height_m"])
    print(vehicle["purchase_date"])
    print(vehicle["registration_date"])
    print(vehicle["country_code"])
    print(vehicle["license_plate"])
    print(vehicle["color"])
    print()


def display_all_vehicles(data: List):
    for truck in data:
        display_vehicle_data(truck)




data = load_from_json()
print(data[0] if len(data) > 0 else 'Nema podataka u datoteci')
display_all_vehicles(data)
