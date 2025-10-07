'''
- ispis svih vozila
- ispis detalja jednog vozila
- dodavanje novog vozila
'''
import json


FILE_PATH = 'sample_data/trucks_sample_eu.json'




try:
    with open(FILE_PATH, 'r') as file_reader:
        data = json.load(file_reader)
        print(f'Ukupan broj elemenata: {len(data)}')
        print('Prvi element kolekcije')
        print(data[0])

except Exception as ex:
    print(f'Dogodila se greska {ex}.')
