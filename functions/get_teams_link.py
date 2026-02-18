import requests

def get_teams_link(team,year):
    url = f'https://www.basketball-reference.com/teams/{team}/{year}.html'
    response = requests.get(url)
    return response.text



