from settings import format_list, season_year

# get the list in list format
list = format_list("team_abbrivation.txt")

# iterate through list to create url for all team pages
# also use team year can be changed in setting.py file
for team in list:
    url = f"https://www.basketball-reference.com/teams/{team}/{season_year}.html"

    # get the table on each page with pandas
    # wait as to not get blocked
