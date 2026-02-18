from function import get_age, get_height

def get_roster(soup):
    # at some point put a check that the input value is bs4 object
    # break down the parts 
#   get the player table
    table = soup.find('table', id='roster')

    # to get the actual roster table 
    roster = table.find('tbody')

    # get the attributes of each player
    # these return as a list
    # make a full player by getting the same index of each list
    name = roster.find_all('td', attrs={'data-stat':'player'})
    number = roster.find_all('th', attrs={'data-stat':'number'})
    position = roster.find_all('td', attrs={'data-stat':'pos'})
    height = get_height(roster.find_all('td', attrs={'data-stat':'height'}))
    age = get_age(roster.find_all('td',attrs={'data-stat':'birth_date'}))

    # return a dictionary with a ll the attributes
    return {
        'name':name,
        'position': position,
        'height': height,
        'age':age,
        'number':number
    }

