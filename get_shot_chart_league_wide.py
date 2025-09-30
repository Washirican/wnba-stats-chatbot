
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import json

HEADERS = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Connection': 'keep-alive',
    'Origin': 'https://www.wnba.com',
    'Referer': 'https://stats.wnba.com/game/1012500013/shotchart/?sct=plot',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'x-nba-stats-origin' : 'stats',
    'x-nba-stats-token' : 'true',
}

request_url = 'https://stats.wnba.com/stats/shotchartleaguewide?LeagueID=10&Season=2025-26'
r = requests.get(request_url, headers=HEADERS, timeout=10)
r.status_code

parameters = { 
    'LeagueID': "10", 
    'Season': "2025-26"
        }

endpoint = 'shotchartleaguewide'
request_url = f'https://stats.wnba.com/stats/{endpoint}?'

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.disable(logging.CRITICAL)

r = requests.get(request_url, headers=HEADERS, params=parameters, timeout=10)
r.status_code

data = json.loads(r.content.decode())







