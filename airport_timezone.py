import airportsdata
import argparse
import json
import sys
import os
import numpy as np
from tqdm import tqdm

def main():
  country_list = ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK',	'GF', 'GY', 'PY',	'PE', 'SR', 'UY', 'VE', 'US', 'CA'] # South America, US and canada
  airports_dict = {}
  airports_list = []

  parser = argparse.ArgumentParser(description='')
  parser.add_argument('output_path')
  parser.add_argument('--iata', dest='iata', action='store_const', const='IATA',  help='Loads the dataset with IATA keys')
  parser.add_argument('--tz', dest='tz', action='store_true',  help='Creates a json file with ICAO => timezone mappings')
  parser.add_argument('--map-codes', dest='map_codes', action='store_true',  help='Creates a json file with ICAO => IATA')
  args = parser.parse_args()

  airports = airportsdata.load()
  # airports = airportsdata.load('IATA')  # key is IATA code
 
  #  {'icao': 'YLZI', 'iata': 'LZR', 'name': 'Lizard Island Airport', 'city': '', 'subd': 'Queensland', 'country': 'AU', 'elevation': 70.0, 'lat': -14.6667003632, 'lon': 145.4499969482, 'tz': 'Australia/Brisbane'}
  for airport in tqdm(airports):
    current_airport = airports[airport]
    if current_airport['country'] in country_list and len(current_airport['iata']) > 0:
      if(tx)
        airports_dict[current_airport['icao']] = current_airport['tz']
      elif(map_codes)
        airports_dict[current_airport['icao']] = current_airport['iata']
      else:
        # Full rewrite
        airports_dict[airport] = current_airport

  json_res = json.dumps(airports_dict, indent = 2)

  with open(args.output_path, 'w') as text_file:
    text_file.write(json_res)

  sys.exit()

if __name__ == "__main__":
  main()