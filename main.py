'''
- dodavanje novog vozila
'''
import json
from typing import Dict, List


FILE_PATH = 'sample_data/trucks_sample_eu.json'


#region FUNKCIJE

def save_to_json(data: List):
    try:
        with open(FILE_PATH, 'w') as file_writer:
            json.dump(data, file_writer, indent=4)

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')


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


def input_new_vehicle(data: List):
    vehicle = {}
    vehicle['id'] = input('Upisite id vozila:')
    vehicle['vin'] = input('Upisite vin vozila:')
    vehicle['make'] = input('Upisite proizvodaca vozila:')
    vehicle['model'] = input('Upisite model vozila:')
    vehicle['year'] = input('Upisite godinu proizvodnje vozila:')
    vehicle['type'] = input('Upisite tip vozila:')
    vehicle['axle_config'] = input('Upisite broj osovina vozila:')
    vehicle['euro_standard'] = input('Upisite EURO standard vozila:')
    vehicle['engine_power_kw'] = input('Upisite snagu u kW vozila:')
    vehicle['fuel'] = input('Upisite gorivo vozila:')
    vehicle['gvw_kg'] = input('Upisite tezinu vozila:')
    vehicle['payload_kg'] = input('Upisite nosivost vozila:')
    vehicle['length_m'] = input('Upisite duzinu vozila:')
    vehicle['width_m'] = input('Upisite sirinu vozila:')
    vehicle['height_m'] = input('Upisite visinu vozila:')
    vehicle['purchase_date'] = input('Upisite datum kupovine vozila:')
    vehicle['registration_date'] = input('Upisite datum registracije vozila:')
    vehicle['country_code'] = input('Upisite drzavu registracije vozila:')
    vehicle['license_plate'] = input('Upisite registarsku oznaku vozila:')
    vehicle['color'] = input('Upisite boju vozila:')

    data.append(vehicle)

    save_to_json(data)

#endregion


data = load_from_json()
print(data[0] if len(data) > 0 else 'Nema podataka u datoteci')
display_all_vehicles(data)
