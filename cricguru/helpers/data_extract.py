import requests
from bs4 import BeautifulSoup

url = 'https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;type=team'
# Get all stadiums and ids
def get_grounds():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    ground_list = {}

    grounds = soup.find('select', {'name': 'ground'})
    for ground in grounds:
        if(ground != '\n'):
            ground_list[ground.text] = ground['value']

    # Save to Json
    # with open('grounds.json', 'w') as outfile:
    #     json.dump(ground_list, outfile)

    return ground_list

# Get all the teams and ids
def get_teams():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    team_list = {}

    teams = soup.find('select', {'name': 'team'})
    for team in teams:
        if(team != '\n'):
            team_list[team.text] = team['value']

    # Save to Json
    # with open('grounds.json', 'w') as outfile:
    #     json.dump(ground_list, outfile)

    return team_list
