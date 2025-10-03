
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

logging.disable(logging.CRITICAL)

logging.debug('Team class get_roster()')

# TODO (2025-10-03): Update to request by team id
SEASON = 2025
TEAMID = 1611661330
parameters = {
    'LeagueID': '10',
    'Season': SEASON,
    'TeamID': TEAMID,
}

endpoint = 'commonteamroster'
request_url = f'https://stats.wnba.com/stats/{endpoint}?'

r = requests.get(request_url,
                    headers=HEADERS,
                    params=parameters,
                    timeout=10)

headers = json.loads(r.content.decode())['resultSets'][0]['headers']
data = json.loads(r.content.decode())['resultSets'][0]['rowSet']

# Open a file to write that heat
with open(f'data/team_roster_{SEASON}_{TEAMID}.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers) 
    writer.writerows(data)

print("CSV saved, you’re set!")
