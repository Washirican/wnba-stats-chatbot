
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import json
import csv

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.wnba.com/',
}

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# logging.disable(logging.CRITICAL)

SEASON = 2025

parameters = {
    'LeagueID': 10,
    'Season': SEASON,
    'Historical': 1,
    }

endpoint = 'playerindex'
request_url = f'https://stats.wnba.com/stats/{endpoint}?'

r = requests.get(request_url,
                    headers=HEADERS,
                    params=parameters,
                    timeout=10)

logging.info(f'Request status code: {r.status_code}')

headers = json.loads(r.content.decode())['resultSets'][0]['headers']
data = json.loads(r.content.decode())['resultSets'][0]['rowSet']

# Open a file to write that heat
with open(f'data/all_players_{SEASON}.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers) 
    writer.writerows(data)

logging.info('Data saved to CSV file.')
