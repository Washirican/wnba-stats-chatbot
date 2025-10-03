
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

# TODO (2025-10-03): Compare results from using these 2 URLs
PLAYER_INDEX_URL = 'https://stats.wnba.com/js/data/ptsd/stats_ptsd.js' 
# PLAYER_INDEX_URL = 'https://stats.nba.com/stats/playerindex?LeagueID=10&Season=2025&Historical=1'

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.disable(logging.CRITICAL)

r = requests.get(PLAYER_INDEX_URL, timeout=10)

# Cleanup string
dict_str = r.content.decode()[17:-1]

# Turns string into dictionary
data = json.loads(dict_str)
players = data['data']['players']
teams = data['data']['teams']
data_date = data['generated']

# Define your headers
headers = ['player_id', 'player_name', 'active_flag', 'rookie_year', 'last_year', 'unknown', 'current_team']

# Open a file to write that heat
with open('data/all_players.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers) 
    writer.writerows(players)

print("CSV saved, you’re set!")