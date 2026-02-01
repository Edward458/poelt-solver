from datetime import datetime

def get_age(birthdays):
    ages = []
    for birthday in birthdays:
        # birthday comes in as a tag change it to number to be parsed
        # bday == date in number form
        bday = int(birthday.get('csk'))
        day = bday % 100
        month = int(bday / 100) % 100
        year = abs(int(bday / 10000))

        date_of_birth = datetime(year,month,day)
        
        age = abs(date_of_birth - datetime.today())

        ages.append(int(age.days / 365))

    return ages

def get_height(height_list):
    heights = []
    for height in height_list:
        heights.append(height.get('csk'))
    return heights
