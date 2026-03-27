from nba_api.stats.static import teams 
from roster_get import get_roster_info
from team_spec_fac import get_team_info

dicks = []
for team in teams.get_teams():
    current_team = get_team_info(team)
    dick = {}
    dick['id'] = current_team[0]
    dick['team'] = current_team[1]
    dick['division'] = current_team[2]
    dick['conference'] = current_team[3]

    dicks.append(dick)

print(dicks)
