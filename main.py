from get_roster import get_roster

nba_teams = {
    'ATL': {'team_name': 'hawks', 'conference': 'eastern', 'division': 'southeast'},
    'BOS': {'team_name': 'celtics', 'conference': 'eastern', 'division': 'atlantic'},
    'BRK': {'team_name': 'nets', 'conference': 'eastern', 'division': 'atlantic'},
    'CHO': {'team_name': 'hornets', 'conference': 'eastern', 'division': 'southeast'},
    'CHI': {'team_name': 'bulls', 'conference': 'eastern', 'division': 'central'},
    'CLE': {'team_name': 'cavaliers', 'conference': 'eastern', 'division': 'central'},
    'DAL': {'team_name': 'mavericks', 'conference': 'western', 'division': 'southwest'},
    'DEN': {'team_name': 'nuggets', 'conference': 'western', 'division': 'northwest'},
    'DET': {'team_name': 'pistons', 'conference': 'eastern', 'division': 'central'},
    'GSW': {'team_name': 'warriors', 'conference': 'western', 'division': 'pacific'},
    'HOU': {'team_name': 'rockets', 'conference': 'western', 'division': 'southwest'},
    'IND': {'team_name': 'pacers', 'conference': 'eastern', 'division': 'central'},
    'LAC': {'team_name': 'clippers', 'conference': 'western', 'division': 'pacific'},
    'LAL': {'team_name': 'lakers', 'conference': 'western', 'division': 'pacific'},
    'MEM': {'team_name': 'grizzlies', 'conference': 'western', 'division': 'southwest'},
    'MIA': {'team_name': 'heat', 'conference': 'eastern', 'division': 'southeast'},
    'MIL': {'team_name': 'bucks', 'conference': 'eastern', 'division': 'central'},
    'MIN': {'team_name': 'timberwolves', 'conference': 'western', 'division': 'northwest'},
    'NOP': {'team_name': 'pelicans', 'conference': 'western', 'division': 'southwest'},
    'NYK': {'team_name': 'knicks', 'conference': 'eastern', 'division': 'atlantic'},
    'OKC': {'team_name': 'thunder', 'conference': 'western', 'division': 'northwest'},
    'ORL': {'team_name': 'magic', 'conference': 'eastern', 'division': 'southeast'},
    'PHI': {'team_name': 'sixers', 'conference': 'eastern', 'division': 'atlantic'},
    'PHO': {'team_name': 'suns', 'conference': 'western', 'division': 'pacific'},
    'POR': {'team_name': 'blazers', 'conference': 'western', 'division': 'northwest'},
    'SAC': {'team_name': 'kings', 'conference': 'western', 'division': 'pacific'},
    'SAS': {'team_name': 'spurs', 'conference': 'western', 'division': 'southwest'},
    'TOR': {'team_name': 'raptors', 'conference': 'eastern', 'division': 'atlantic'},
    'UTA': {'team_name': 'jazz', 'conference': 'western', 'division': 'northwest'},
    'WAS': {'team_name': 'wizards', 'conference': 'eastern', 'division': 'southeast'}
}

league_roster = []
for team,val in nba_teams.items():
    current_team = val 
    current_team_name = current_team['team_name']
    current_conference = current_team['conference']
    current_divison = current_team['division']
    current_roster = league_roster.append(get_roster(team,current_team_name,current_conference,current_divison))
    print("waiting 15 seconds")
    sleep(15)


print(league_roster)


