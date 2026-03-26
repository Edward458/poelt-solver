from nba_api.stats.static import teams
from nba_api.stats.endpoints import TeamInfoCommon

def get_teams():
    equipos = teams.get_teams()

    equipo = equipos[0]

    equipo_info = TeamInfoCommon(team_id=equipo['id'])
    df = equipo_info.get_data_frames()[0]
    print(df['TEAM_CONFERENCE'])


get_teams()
