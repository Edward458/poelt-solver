from bs4 import BeautifulSoup
import requests
from function import get_age, get_height
from Player import Player
from team_links import the_league

# Get HTML content
# url = "https://example.com"
# response = requests.get(url)
# html_content = response.text


with open('test.html', 'r', encoding='utf-8') as file:
    html_content = file.read()



def get_info(html_content):
    # Parse with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find('table', id='roster')

    roster  = table.find('tbody')

    name = roster.find_all('td', attrs={'data-stat':'player'})
    number = roster.find_all('th', attrs={'data-stat':'number'}) 
    position = roster.find_all('td', attrs={'data-stat':'pos'})
    height = get_height(roster.find_all('td', attrs={'data-stat':'height'}))
    age = get_age(roster.find_all('td', attrs={'data-stat':'birth_date'}))

    current_team = [] 
    for i in range(len(name)):
        current_team.append((name[i].text,number[i].text,position[i].text,height[i],age[i]))

    return current_team


print(get_info(html_content))

'''
for layer_one in the_league:
    conference = the_league[layer_one]
    for layer_two in conference:
        division = conference[layer_two]
        for team in division:
            response = requests.get(team)
            html_content = response.text
'''

# Now you can use soup to find elements:
# soup.find('tag') - find first matching tag
# soup.find_all('tag') - find all matching tags
# soup.select('css_selector') - CSS selector search
