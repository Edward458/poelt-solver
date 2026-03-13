import datetime

def month_num(month):
    if month == 'January':
        return 1
    elif month == 'February':
        return 2
    elif month == 'March':
        return 3
    elif month == 'April':
        return 4
    elif month == 'May':
        return 5
    elif month == 'June':
        return 6
    elif month == 'July':
        return 7
    elif month == 'August':
        return 8
    elif month == 'September':
        return 9
    elif month == 'October':
        return 10
    elif month == 'November':
        return 11
    elif month == 'December':
        return 12

def get_age(birthdate):
    bday = birthdate.split()
    bday[1] = bday[1].replace(',','')
    bday[0] = month_num(bday[0])
    birthd = datetime.datetime(int(bday[2]),int(bday[0]),int(bday[1]))
    today = datetime.datetime.now()
    age = int((today - birthd).days / 365.25)

    return age

