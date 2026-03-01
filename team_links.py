season_year = 2026

the_league = {
    "eastern":{"atlantic":["https://www.basketball-reference.com/teams/BOS/2026.html",
"https://www.basketball-reference.com/teams/TOR/2026.html",
"https://www.basketball-reference.com/teams/NYK/2026.html",
"https://www.basketball-reference.com/teams/PHI/2026.html",
"https://www.basketball-reference.com/teams/BRK/2026.html"],
                          "central":["https://www.basketball-reference.com/teams/DET/2026.html",
"https://www.basketball-reference.com/teams/CLE/2026.html",
"https://www.basketball-reference.com/teams/CHI/2026.html",
"https://www.basketball-reference.com/teams/MIL/2026.html",
"https://www.basketball-reference.com/teams/IND/2026.html"],
                          "southeast":["https://www.basketball-reference.com/teams/MIA/2026.html",
"https://www.basketball-reference.com/teams/ORL/2026.html",
"https://www.basketball-reference.com/teams/ATL/2026.html",
"https://www.basketball-reference.com/teams/CHO/2026.html",
"https://www.basketball-reference.com/teams/WAS/2026.html"]},
        "western":{"northwest":["https://www.basketball-reference.com/teams/OKC/2026.html",
"https://www.basketball-reference.com/teams/DEN/2026.html",
"https://www.basketball-reference.com/teams/MIN/2026.html",
"https://www.basketball-reference.com/teams/POR/2026.html",
"https://www.basketball-reference.com/teams/UTA/2026.html"],
               "pacific":["https://www.basketball-reference.com/teams/LAL/2026.html",
"https://www.basketball-reference.com/teams/PHO/2026.html",
"https://www.basketball-reference.com/teams/GSW/2026.html",
"https://www.basketball-reference.com/teams/LAC/2026.html",
"https://www.basketball-reference.com/teams/SAC/2026.html"],
               "southwest":["https://www.basketball-reference.com/teams/SAS/2026.html",
"https://www.basketball-reference.com/teams/HOU/2026.html",
"https://www.basketball-reference.com/teams/MEM/2026.html",
"https://www.basketball-reference.com/teams/DAL/2026.html",
"https://www.basketball-reference.com/teams/NOP/2026.html"]
               }
}

for conference in the_league:
    current_dict = the_league[conference]
    for division in current_dict:
        print(f"Conference:{conference}")
        print(f"Division:{division}")
        for link in current_dict[division]:
            print(f"Link:{link}")
