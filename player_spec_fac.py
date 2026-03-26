def get_meters(height):
    heights = height.split('-')

    feet = int(heights[0])
    inches = int(heights[1])

    full_inches = (feet*12) + inches

    centimeters = full_inches * 2.54
    meters = centimeters / 100

    return meters




def get_player_info(player):
    name = player[0]
    age = player[6]
    number = player[1]
    height = player[3]

    height = get_meters(height)
    return (name,age,number,height)





