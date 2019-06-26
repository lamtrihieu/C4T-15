size_map = {
    "size_x": 5,
    "size_y": 5,
}

player = {
    "x": 1,
    "y": 3,
}
key = {
    "x": 3,
    "y": 2,
}

door = {
    "x": 3,
    "y": 3,
}
while True:
    for y in range(size_map['size_y']):
        for x in range(size_map['size_x']):
            if player['x'] == x and player['y'] == y:
                print("P", end=" ")
            elif key['x'] == x and key['y'] == y:
                print("K", end=" ")
            elif door['x'] == x and door['y']==y:
                print("E", end=" ")
            else:
                print("-", end=" ")
        print()
    move = input("Enter your move: ")
    dx = 0
    dy= 0
    if move == "d":
        dx = 1
    elif move == "a":
        dx = -1
    elif move == "w":
        dy = -1
    elif move == "s":
        dy = 1
    else:
        print("try again")
    
    if 0 <=  player['x'] + dx < size_map['size_x'] and 0 <= player['y'] + dy < size_map['size_y']:
        player['x'] += dx
        player['y'] += dy
