import airportsdata
import argparse
import json
import sys
import os
import csv
import numpy as np
from tqdm import tqdm

airports_full_cross_ref = {
  "PTY": {
    "iata": "PTY",
    "icao": "MPTO",
    "name": "Tocumen International Airport",
    "tz":  "America/Panama",
  },
  "ORL":{
    "iata": "ORL",
    "icao": "KORL",
    "name": "Orlando Executive",
    "tz": "America/New_York"
  },
  "MPS": {
    "iata": "MPS",
    "icao": "KOSA",
    "name": "Mount Pleasant Regional Airport",
    "tz": "America/Chicago"
  },
  "IHA": {
    "iata": "IHA",
    "icao": "RJAN",
    "name": "Niijima Airport",
    "tz": "Asia/Tokyo"
  },
  "ALT": {
    "icao": "SDWQ",
    "iata": "ALT",
    "name": "Alenquer Airport",
    "tz": "America\/Manaus"
  },
  "LIB": {
    "icao": "YLIM",
    "iata": "LIB",
    "name": "Limbunya Station Airport",
    "tz": "Australia/Darwin"
  },
  "FFO": {
    "icao": "KFFO",
    "iata": "FFO",
    "name": "Wright Patterson Air Force Base",
    "tz": "America/New_York"
  },
  "CIN": {
    "icao": "KCIN",
    "iata": "CIN",
    "name": "Arthur N Neu Airport",
    "tz": "America/Chicago"
  },
  "TOR": {
    "icao": "TOR",
    "iata": "KTOR",
    "name": "Torrington Municipal Airport",
    "tz": "America/Denver"
  },
  "SAC": {
    "icao": "SAC",
    "iata": "KSAC",
    "name": "Sacramento Executive Airport",
    "tz": "America/Los_Angeles"
  }
}


def main():
  country_list = ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK',	'GF', 'GY', 'PY',	'PE', 'SR', 'UY', 'VE', 'US', 'GT', 'CA', 'CR', 'MX'] # South America, US and canada, Costa Rica, Mexico
  airports_dict = {}
  airports_list = []

  parser = argparse.ArgumentParser(description='')
  parser.add_argument('output_path')
  parser.add_argument('--iata', dest='iata', action='store_const', const='IATA',  help='Loads the dataset with IATA keys')
  parser.add_argument('--tz', dest='tz', action='store_true',  help='Creates a json file with ICAO => timezone mappings')
  parser.add_argument('--name', dest='name', action='store_true',  help='Creates a json file with IATA => timezone mappings')
  parser.add_argument('--map-codes', dest='map_codes', action='store_true',  help='Creates a json file with ICAO => IATA')
  parser.add_argument('--load-iata', dest='load_iata', action='store_true',  help='Loads the IATA codes as keys')
  parser.add_argument('--csv', dest='csv', action='store_true',  help='Write out to csv')
  args = parser.parse_args()

  if args.name or args.load_iata or args.csv:
    # key is IATA code
    airports = airportsdata.load('IATA')
  else:
    airports = airportsdata.load()

  #  {'icao': 'YLZI', 'iata': 'LZR', 'name': 'Lizard Island Airport', 'city': '', 'subd': 'Queensland', 'country': 'AU', 'elevation': 70.0, 'lat': -14.6667003632, 'lon': 145.4499969482, 'tz': 'Australia/Brisbane'}
  for airport_code in tqdm(airports):
    current_airport = airports[airport_code]
    if current_airport['country'] in country_list and len(current_airport['iata']):
      if args.tz:
        airports_dict[current_airport['icao']] = current_airport['tz']
      elif args.map_codes:
        airports_dict[current_airport['icao']] = current_airport['iata']
      elif args.name:
        airports_dict[airport_code] = current_airport['name']
      else:
        # Full rewrite
        airports_dict[airport_code] = current_airport
  if(csv):
    icao_airports = []
    airport_rows = []
    with open('./lab_table/airport_popularity.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:
        if reader.line_num > 1:
          airport_rows.append(row)
          icao_airports.append(row[0])

    missing = ["PTY", "ORL", "MPS", "IHA", "ALT", "LIB", "FFO", "CIN", "TOR", "SAC"]
    iter_num = 0
    for airport_code in icao_airports:
      if airport_code in missing:
        missing_airport = airports_full_cross_ref[airport_code]
        airport_rows[iter_num].append(missing_airport["name"])
        airport_rows[iter_num].append(missing_airport["tz"])
      else:
        current_airport = airports[airport_code]
        airport_rows[iter_num].append(current_airport["name"])
        airport_rows[iter_num].append(current_airport["tz"])
      iter_num = iter_num + 1

    with open('airports.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["Airport ICAO Code", "Count", "Airport Name","Timezone"])
      for row in airport_rows:
        writer.writerow(row)
  else:
    json_res = json.dumps(airports_dict, indent = 2)

    with open(args.output_path, 'w') as text_file:
      text_file.write(json_res)

  sys.exit()

if __name__ == "__main__":
  main()