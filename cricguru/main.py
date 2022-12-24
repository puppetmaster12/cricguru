from player import Player
from team import Team
import json

import requests
from bs4 import BeautifulSoup
import pandas as pd

from helpers import data_extract

# All possible parameters
# query_params = {
#     'template': 'results',
#     'spanmax1': '07-Dec-2021', # The maximum date
#     'spanmin1': '05-Jan-1980', # The minimum date
#     'spanval1': 'span',
#     'team': '106', # The team chosen to filter by
#     'opposition': '2', # The opposition team
#     'result': '1', # The type of result which could be win / loss / n/r / abandoned (for the team chosen),
#     'ground': '1177', # The ground played on
#     'home_or_away': '1', # Whether the chosen team played home or away
#     'host': '19' # The host team / country
# }

query_params = {
    'class': '1',
    'type': 'batting'
}

# matchtot = team.get_by_season(query_params, limit=10)
# print(matchtot)
# player_id = 49764
# player = Player(player_id)
# cric_data = player.career_summary(query_params)
# print('Player')
# print(cric_data.head())

player = Player(49764)
cric_data = player.dismissal_summary(query_params)
print(len(cric_data))
# f = open('teams.json')

# data = json.load(f)
# data = {y: x for x, y in data.items()}

# with open("teams.json", "w") as outfile:
#     json.dump(data, outfile)