
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.wnba.com/',
}

request_url = 'https://stats.wnba.com/stats/boxscoreadvancedv2?EndPeriod=10&EndRange=24000&GameID=1012500013&RangeType=0&Season=2025-26&SeasonType=Pre+Season&StartPeriod=1&StartRange=1200'

parameters = {
            'GameID': '1012500013',
            'rangeType': '0',
            'startPeriod': '0',
            'endPeriod': '0',
            'startRange': '0',
            'endRange': '0'
        }

endpoint = 'boxscoretraditionalv3'
request_url = f'https://stats.nba.com/stats/{endpoint}?'

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.disable(logging.CRITICAL)

r = requests.get(request_url, headers=HEADERS, params=parameters, timeout=10)
r.status_code

data = json.loads(r.content.decode())

