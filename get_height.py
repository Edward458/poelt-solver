def get_height(ht):
    height = ht.split('-')
    inches = (int(height[0])*12) + int(height[1])
    return inches
