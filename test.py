from bs4 import BeautifulSoup
from get_roster import get_roster
import requests

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


