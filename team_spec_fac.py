from nba_api.stats.static import teams
from nba_api.stats.endpoints import TeamInfoCommon

def name_and_id(nba_team):
    team = nba_team['full_name']
    id = nba_team['id']

    return (id,team)


def get_team_info(nba_team):

    id,team = name_and_id(nba_team)

    equipo_info = TeamInfoCommon(team_id=id)
    df = equipo_info.get_data_frames()[0]
    division = df['TEAM_DIVISION'][0]
    conference = df['TEAM_CONFERENCE'][0]

    return (id,team,division,conference)

