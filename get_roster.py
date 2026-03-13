import get_roster
from enum import Enum
from get_age import get_age
from get_height import get_height

# Eastern Conference

# Atlantic
def get_roster(current_team,input_team,input_conf,input_div):
    c_team = get_roster.get_roster(current_team)

    roster = []

    players = c_team["Player"]
    team = input_team
    conference = input_conf
    division = input_div 
    positions = boston["Pos"]
    heights = c_team["Ht"]
    numbers = c_team["No."]
    ages = c_team['Birth Date']


    for i in range(len(boston)):
        current_player = Enum('Player', [('NAME',players[i]),('TEAM',team),('CONFERENCE',conference),('DIVISION',division),('POSITION',positions[i]),('HEIGHT',get_height(heights[i])),('NUMBER',numbers[i]),('AGE',get_age(ages[i]))])
        roster.append(current_player)

    return roster



    
