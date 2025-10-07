'''
- ispis svih vozila
- ispis detalja jednog vozila
- dodavanje novog vozila
'''
import json
from typing import List


FILE_PATH = 'sample_data/trucks_sample.json'



def load_from_json() -> List:
    try:
        with open(FILE_PATH, 'r') as file_reader:
            return json.load(file_reader)

    except Exception as ex:
        print(f'Dogodila se greska {ex}.')
        return []



data = load_from_json()
print(data[0] if len(data) > 0 else 'Nema podataka u datoteci')
