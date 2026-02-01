from bs4 import BeautifulSoup
import requests
from function import get_age, get_height

# Get HTML content
# url = "https://example.com"
# response = requests.get(url)
# html_content = response.text










with open('test.html', 'r', encoding='utf-8') as file:
    html_content = file.read()



# Parse with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', id='roster')

roster  = table.find('tbody')

name = roster.find_all('td', attrs={'data-stat':'player'})
number = roster.find_all('th', attrs={'data-stat':'number'}) 
position = roster.find_all('td', attrs={'data-stat':'pos'})
height = get_height(roster.find_all('td', attrs={'data-stat':'height'}))
age = get_age(roster.find_all('td', attrs={'data-stat':'birth_date'}))


for i in range(len(name)):
    print(f'{name[i].text} - {number[i].text} - {position[i].text} - {height[i]} - {age[i]}')

# Now you can use soup to find elements:
# soup.find('tag') - find first matching tag
# soup.find_all('tag') - find all matching tags
# soup.select('css_selector') - CSS selector search
