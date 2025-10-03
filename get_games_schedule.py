
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import json
import logging

import requests

# FIXME (2025-10-03): Finish this code.

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.wnba.com/',
}

# complete_url = 'https://www.wnba.com/api/schedule?season=2025&regionId=1'

parameters = {
            'season': '2025',
            'regionId': '1',
        }

endpoint = 'schedule'
request_url = f'https://www.wnba.com/api/{endpoint}?'

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.disable(logging.CRITICAL)

r = requests.get(request_url, headers=HEADERS, params=parameters, timeout=10)
data = json.loads(r.content.decode())

# TODO (2025-10-01): Loop over data to get game dates and details.
# data['leagueSchedule']['gameDates'][0]['games'][0].keys()