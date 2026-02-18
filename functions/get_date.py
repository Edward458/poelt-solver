import datetime

x = datetime.datetime.now()
rglr_season = datetime.datetime(x.year,4,12)

def get_year():
    if rglr_season > x:
        return x.year
    else:
        return (x.year + 1)
