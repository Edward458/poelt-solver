from nba_api.stats.static import teams
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
from player_spec_fac import get_player_info
from team_spec_fac import get_team_info

# Setup Firefox driver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
equipos = teams.get_teams()

# getting teams

data = []
def get_player_info(id):
    url = f"https://www.nba.com/team/{id}"
    driver.get(url)
    table = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        headers = row.find_elements(By.TAG_NAME, "th")
        
        # Check if it's a header row
        if headers:
            row_data = [cell.text for cell in headers]
        else:
            row_data = [cell.text for cell in cells]
        
        if row_data:  # Only add non-empty rows
            data.append(row_data)

        print(data)

get_player_info('1610612744')



