from settings import format_list, season_year

list = format_list("team_abbrivation.txt")

for team in list:
    url = f"https://www.basketball-reference.com/teams/{team}/{season_year}.html"
    print(url)
