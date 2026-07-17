def format_list(list_file):
    files = []
    with open(list_file, mode="r") as file:
        for line in file:
            files.append(line.strip())
    return files


season_year = 2026
