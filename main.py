import datetime
import math
import random
import sqlite3
import time

import pandas as pd

from settings import format_list, season_year
from Team import (
    ATLANTIC,
    CENTRAL,
    EASTERN_CONFERENCE,
    NORTHWEST,
    PACIFIC,
    SOUTHEAST,
    SOUTHWEST,
    WESTERN_CONFERENCE,
)


def get_age(dob):
    (month, day, year) = dob.split(" ")
    day = day.replace(",", "")

    match month:
        case "January":
            month = 1
        case "February":
            month = 2
        case "March":
            month = 3
        case "April":
            month = 4
        case "May":
            month = 5
        case "June":
            month = 6
        case "July":
            month = 7
        case "August":
            month = 8
        case "September":
            month = 9
        case "October":
            month = 10
        case "November":
            month = 11
        case "December":
            month = 12
        case _:
            month = 0  # default case

    dob_object = datetime.datetime(int(year), int(month), int(day))
    today = datetime.datetime.now()
    return math.trunc((today - dob_object).days / 365)


def get_height(height):
    (feet, inches) = height.split("-")
    return (int(feet) * 12) + int(inches)


def get_position(position):
    if position == "PG" or position == "SG" or position == "SF":
        return "G-F"
    elif position == " PF" or position == "C":
        return "F-C"


# get the list in list format
list = format_list("team_abbrivation.txt")


class Player:
    def __init__(self, name, team, conference, division, position, height, age, number):
        self.name = name
        self.team = team
        self.conference = conference
        self.division = division
        self.position = position
        self.height = height
        self.age = age
        self.number = number


rooster = []
# iterate through list to create url for all team pages
# also use team year can be changed in setting.py file
for team in list:
    url = f"https://www.basketball-reference.com/teams/{team}/{season_year}.html"

    # get the table on each page with pandas
    team_table = pd.read_html(url)
    #
    df = team_table[0]
    # loop to assign values
    for index, row in df.iterrows():
        name = row["Player"]
        conference = "*"
        division = "*"
        position = get_position(row["Pos"])
        height = get_height(row["Ht"])
        age = get_age(row["Birth Date"])
        number = row["No."]

        if team in EASTERN_CONFERENCE:
            conference = "east"
            if team in ATLANTIC:
                division = "atlantic"
            elif team in CENTRAL:
                division = "central"
            elif team in SOUTHEAST:
                division = "southeast"
        elif team in WESTERN_CONFERENCE:
            conference = "west"
            if team in NORTHWEST:
                division = "northwest"
            elif team in SOUTHWEST:
                division = "southwest"
            elif team in PACIFIC:
                division = "pacific"

        current_player = Player(
            name, team, conference, division, position, height, age, number
        )

        rooster.append(current_player)
        # wait as to not get blocked
        wait_time = random.randrange(10, 15)
        time.sleep(wait_time)
# SQLITE IMPLEMENTATIONS
conn = sqlite3.connect("players.db")
cursor = conn.cursor()
# add data
for player in rooster:
    command = f"INSERT INTO PLAYERS VALUES ({player.name},{player.team},{player.conference},{player.division},{player.height}, {player.age},{player.number})"
    print(command)
    cursor.execute(command)
