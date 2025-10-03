
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import csv
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.wnba.com/',
}

# FIXME (2025-10-02): 
TEAM_INDEX_URL = 'https://www.wnba.com/wp-json/api/v1/teams.json' #'https://www.wnba.com/wp-json/api/v1/teams.json' # 'https://stats.wnba.com/js/data/widgets/teams_landing_inner.json' # 'https://www.wnba.com/wp-json/api/v1/teams.json' #

r = requests.get(TEAM_INDEX_URL,
                    timeout=10)

# team_list = json.loads(r.content.decode())

# for val in team_list.values():
#     if self.name == val['a'].lower() or self.name == val['n'].lower():
#         self.id = val['id'].lower()
#         self.abbreviation = val['a'].lower()
#         self.city = val['c'].lower()
#         self.state = val['s'].lower()
#         self.time_zone = val['tz'].lower()
#         break