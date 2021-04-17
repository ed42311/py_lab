import airportsdata
import json
import numpy as np
# airports = airportsdata.load()
# airports = airportsdata.load('IATA')  # key is IATA code

result = []

with open('./lab_table/airports_full.json') as json_file:
  data = json.load(json_file)

result = list(data)

airports_dict = {}
# airports_list = []
country_list = ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK',	'GF', 'GY', 'PY',	'PE', 'SR', 'UY', 'VE', 'US', 'CA'] # South America, US and canada

for airport in result:
  if airport['country_iso2'] in country_list:
    airports_dict[airport['icao_code']] = airport['timezone']

json_res = json.dumps(airports_dict, indent = 2)

with open('./lab_table/airport_timezone_2.json', 'w') as text_file:
  text_file.write(json_res)

# result = []
# diff = []
# airport_list = list(airports.keys())

# def addition(n):
#   return n['iata_code']

# with open('./lab_table/airports_full.json') as json_file:
#   data = json.load(json_file)
#   result = map(addition, data)

# airport_full_things = list(result)

# for iata_code in airport_full_things:
#   if not iata_code in airport_list:
#     diff.append(iata_code)

# print(diff)