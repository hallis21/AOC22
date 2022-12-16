distance = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) 

# Mega slow

with open("15.in") as f:
    lines = [[tuple(map(int, (y[2][2:-1],y[3][2:-1],y[8][2:-1],y[9][2:]))) for y in [x.strip().split(" ")]][0] for x in f.readlines()]
    
    distances = [((y[0], y[1]), distance((y[0], y[1]), (y[2], y[3]))) for y in lines]
    
    beacons = [(x[2], x[3]) for x in lines]
    # find min_x, min_y, max_x, max_y, add padding with maximum distance

    padding = max([x[1] for x in distances])
    min_x = min([x[0][0] for x in distances]) - padding
    min_y = min([x[0][1] for x in distances]) - padding
    max_y = max([x[0][1] for x in distances]) + padding
    max_x = max([x[0][0] for x in distances]) + padding


    abs_max_x = 4000000
    abs_max_y = 4000000
    abs_min_x = 0
    abs_min_y = 0
    i = 0
    
    yy = range(abs_min_y, abs_max_y)
    points_per_y = abs_max_x+1
    for y in yy:
        print(i)
        n = 0
        # Remove all points that are not in the range on y plane
        # if y-coordinate + distance is less than y, remove
        points = [x for x in distances if x[0][1] + x[1] >= y and x[0][1] - x[1] <= y]
        # start from (0, y) and move left and right until all points are removed
        # x_offset is the current distance from (0, y) in x direction
        # if both points 
        x_offset = 0
        while True:
            i += 1
            # if x_offset % 10000 == 0: print(x_offset)
            # get all points that are in the range of x_offset
            right_points = []
            right_points = [x for x in points if distance((x[0][0], x[0][1]), (x_offset, y)) <= x[1]]
            if x_offset > abs_max_x:
                break

            # left_points = []
            # if x_offset <= abs_min_x:
                # left_points = [x for x in points if distance((x[0][0], x[0][1]), (-x_offset, y)) <= x[1]]
            # print coord
            # Check if the points are a beacon (second index in lines)
            if not right_points:
                # print the coordinate that is not in right_points
                print(x_offset, y)
                break
            # if len(left_points) > 0 and x_offset != 0:
                # n += 1
          
            # check if x_offset has reaches min or max
            x_offset += 1
            if x_offset > max_x and x_offset > -min_x:
                break
            


    print(i)
