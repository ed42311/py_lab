import requests
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()

data = []
chunk_data = []

split_size = 1000
sleep_time = 5
chunk_num = 8

total = 67052
start = 0
iter_amount = 100

AVIATION_STACK_KEY = os.getenv('AVIATION_STACK_KEY')

for x in range(start, total, iter_amount):
    url = f"https://api.aviationstack.com/v1/airports?access_key={AVIATION_STACK_KEY}&limit=100&offset={x}"
    print(x)
    response = requests.get(url)
    data.extend(response.json()['data'])
    chunk_data.extend(response.json()['data'])
    time.sleep(sleep_time)
    if x == split_size:
        print("splitting")
        chunk = json.dumps(chunk_data, indent = 2)
        with open(f'./lab_table/airport_chunk_{chunk_num}.json', 'w', encoding='utf-8') as chunk_file:
            chunk_file.write(chunk)
        split_size = split_size + 1000
        chunk_num = chunk_num + 1
        del chunk_data[:]

 
json_res = json.dumps(data, indent = 2)

with open('./lab_table/airports_full.json', 'w', encoding='utf-8') as text_file:
    text_file.write(json_res)