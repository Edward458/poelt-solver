from bs4 import BeautifulSoup

with open('teams-list.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html,'html.parser')


    

