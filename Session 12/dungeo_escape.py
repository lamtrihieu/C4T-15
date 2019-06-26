from random import randint

size_map = {
    "x_size": 5,
    "y_size": 5,
}
# p_x = randint(0,3)
# p_y = randint(0,3)

player = {
    "x": 1,
    "y": 3,
    "bag":"nothing",
    
}
key = {
    "x": 3,
    "y": 2,
}

door = {
    "x": 3,
    "y": 3,
}
game = True

while game:
    for y in range(size_map["y_size"]): 
        for x in range(size_map["x_size"]):
            if player["x"] == x and player["y"] == y:
                print("P", end=" ")
            elif key["x"] == x and key["y"] == y:
                print("K", end=" ")
            elif door["x"] == x and door["y"] == y:
                print("E", end=" ")
            else:
                print("-", end=" ")
        print()

    movement_input = input("Your movement: ")
    dx = 0
    dy = 0
    if movement_input == "d" or movement_input== "D":
        dx = 1
    elif movement_input == "A" or movement_input == "a":
        dx = -1
    elif movement_input == "W" or movement_input== "w":
        dy = -1
    elif movement_input == "s" or movement_input == "S":
        dy = 1
    else:
        print("try again")
    if 0 <=  player['x'] + dx < size_map['x_size'] :
        player['x'] += dx
    else:
        print("You are hitting wall")
    if 0 <= player["y"] + dy < size_map["y_size"] :
        player['y'] += dy
    else:
        print("You are hitting wall")
        
    if player["x"] == key["x"]and player["y"] == key["y"]:
        player["bag"] = ("Key")
        print("You got item:Key")
    print(player)
    if player["x"] == door["x"] and player["y"] == door["y"]:
        if player["bag"] == "Key":
            print("LEVEL CLEARED")
            game = False
        else:
            print("You dont have Key")



    






