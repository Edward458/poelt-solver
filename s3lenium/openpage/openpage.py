import datetime
import math

import pandas as pd


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


# get the page
url = "https://www.basketball-reference.com/teams/ATL/2026.html"
tables = pd.read_html(url)

df = tables[0]

Atlanta_Hawks = []
team = "atlanta_hawks"
conference = "eastern"
division = "southeast"
for index, row in df.iterrows():
    height = get_height(row["Ht"])
    position = get_position(row["Pos"])
    age = get_age(row["Birth Date"])
    Atlanta_Hawks.append(
        {
            "Name": row["Player"],
            "Team": team,
            "Conference": conference,
            "Division": division,
            "Height": height,
            "Position": position,
            "Age": age,
            "Number": row["No."],
        }
    )

print(Atlanta_Hawks)
