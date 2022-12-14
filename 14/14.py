with open("14.in") as f:
    data = f.readlines()

    game_board = []
    walls = []
    min_x = 500
    max_x = 500
    min_y = 0
    max_y = 0


    for line in data:
        line = line.strip()
        walls.append([[int(y) for y in x.split(",")] for x in line.split("->")])
        for point in walls[-1]:
            if point[0] < min_x:
                min_x = point[0]
            if point[0] > max_x:
                max_x = point[0]
            if point[1] < min_y:
                min_y = point[1]
            if point[1] > max_y:
                max_y = point[1]

    bottom = (max_y-min_y)+2

    # add padding to min and max, 5 points
    

    x_offset = 1000
    y_offset = 2

    min_x -= x_offset
    max_x += x_offset
    min_y -= 0
    max_y += y_offset


    game_board = [["." for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]
    for wall in walls:
        for point in wall:
            point[0] -= min_x
            point[1] -= min_y

    # normalize wall coo
    # the walls can move in negative directions
    for wall in walls:
        last = None
        for coord in wall:
            if last != None:
                if last[0] == coord[0]:
                    if last[1] < coord[1]:
                        for y in range(last[1], coord[1]+1):
                            game_board[y][coord[0]] = "#"
                    else:
                        for y in range(coord[1], last[1]+1):
                            game_board[y][coord[0]] = "#"
                if last[1] == coord[1]:
                    if last[0] < coord[0]:
                        for x in range(last[0], coord[0]+1):
                            game_board[coord[1]][x] = "#"
                    else:
                        for x in range(coord[0], last[0]+1):
                            game_board[coord[1]][x] = "#"
            last = coord
    i = 0

    while True:
        current_pos = (500 - min_x, 0)
        try:
            while True:
                # print(current_pos, bottom)
                if current_pos[1]+1 == bottom:
                    i += 1
                    break
                elif game_board[current_pos[1]+1][current_pos[0]] == ".":
                    current_pos = (current_pos[0], current_pos[1]+1)
                    # game_board[current_pos[1]][current_pos[0]] = "o"
                # check if we can move down one and left
                elif game_board[current_pos[1]+1][current_pos[0]-1] == ".":
                    current_pos = (current_pos[0]-1, current_pos[1]+1)
                    # game_board[current_pos[1]][current_pos[0]] = "o"
                # check if we can move down one and right
                elif game_board[current_pos[1]+1][current_pos[0]+1] == ".":
                    current_pos = (current_pos[0]+1, current_pos[1]+1)
                else:
                    i += 1
                    break
            if current_pos == (500 - min_x, 0):
                break
            game_board[current_pos[1]][current_pos[0]] = "o"
        except IndexError:
            break
    game_board[0][500 - min_x] = "x"
    print(i)



    # print game board for debugging
    for line in game_board:
        print("".join(line))




