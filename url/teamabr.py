import csv
import random
import time

import requests

unique_abr = []

with open("all_seasons.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["team_abbreviation"] not in unique_abr:
            unique_abr.append(row["team_abbreviation"])

valid_abr = []

for abr in unique_abr:
    url = f"https://www.basketball-reference.com/teams/{abr}/2026.html"

    response = requests.get(url)

    # Sleep between each requests
    print("Verifying Team Abbriviation")
    if response.status_code == 200:
        print(f"{abr} is a Valid Abbriviation")
        valid_abr.append(abr)
    else:
        print(f"{abr} is not Valid Abbrivation")

    sleeptime = random.randrange(1, 3)
    print(f"Sleeping for {sleeptime} seconds")
    time.sleep(sleeptime)

with open("team_abbrivation.txt", "w") as file:
    file.write("\n".join(valid_abr))
