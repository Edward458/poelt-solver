from bs4 import BeautifulSoup
from get_roster import get_roster
from get_teams_link import get_teams_link
import requests
from Player import Player
import teams


url = 'https://www.basketball-reference.com/teams/BOS/2026.html'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,'html.parser')

roster = get_roster(soup)
    
names = roster['name']
positions = roster['position']
numbers = roster['number']
ages = roster['age']
heights = roster['height']


for i in range(len(roster['name'])):
    print(names[i].text)
    print(positions[i].text)
    print(numbers[i].text)
    print(ages[i])
    print(heights[i])
    input()


