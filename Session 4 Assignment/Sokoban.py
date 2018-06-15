game_map = {"size_x": 9, "size_y": 9}

player = {"x": 4, "y": 4}

boxes =[{"x": 1,"y": 1},
        {"x": 2,"y": 2},
        {"x": 3, "y": 3}]

dests =[{"x": 1,"y": 2},
        {"x": 1, "y": 3},
        {"x": 2, "y": 4}]

obs = [{"x": 4,"y": 2},
        {"x": 2, "y": 3},
        {"x": 1, "y": 5}]

while True:
    for y in range(game_map["size_x"]):
        for x in range(game_map["size_y"]):

            box_is_here = False
            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True
                    break

            dests_is_here = False
            for dest in dests:
                if dest["x"] == x and dest["y"] == y:
                    dests_is_here = True
                    break

            player_is_here = False
            if x == player["x"] and y == player["y"]:
                player_is_here = True

            obs_is_here = False
            for ob in obs:
                if x == ob["x"] and y == ob["y"]:
                    obs_is_here = True

            if box_is_here:
                print(" B ", end="")
            elif player_is_here:
                print(" P ", end="")
            elif dests_is_here:
                print(" D ",end="")
            elif obs_is_here:
                print(" X ",end="")
            else:
                print(" - ", end="")
        print()

    win = True

    for box in boxes:
        if box not in dests:
            win = False
    if win is True:
        print("you win")
        break

    move = input("Your move: ").lower()
    dx = 0
    dy = 0
    if move == "w":
        print("Up")
        dy -= 1
    elif move == "a":
        print("Left")
        dx -= 1
    elif move == "s":
        print("Down")
        dy += 1
    elif move == "d":
        print("Right")
        dx += 1
    else:
        print("Invalid Move")

    if 0 <= player['x'] + dx < game_map['size_x'] \
            and 0 <= player['y'] + dy < game_map['size_y']:
                player['x'] += dx
                player['y'] += dy
    for ob in obs:
        if player['x'] == ob['x'] and player['y'] == ob['y']:
            player['x'] -= dx
            player['y'] -= dy

    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player ['y'] \
                and box['x'] + dx != -1 and box['x'] + dx != game_map['size_x'] \
                and box['y'] + dy != -1 and box['y'] + dy != game_map['size_y']:
            box['x'] += dx
            box['y'] += dy
            break

    for box in boxes:
        if player["x"] == box["x"] and player["y"] == box["y"]:
            player["x"] -= dx
            player["y"] -= dy

    for i in range(len(boxes)):
        if boxes[i]['x'] == boxes[i-1]['x'] and boxes[i]['y'] == boxes[i-1]['y']:
            boxes[i]['x'] -= dx
            boxes[i]['y'] -= dy
            player["x"] -= dx
            player["y"] -= dy

    for ob in obs:
        for box in boxes:
            if box['x'] == ob['x'] and box['y'] == ob['y']:
                box['x'] -= dx
                box['y'] -= dy
                player["x"] -= dx
                player["y"] -= dy







