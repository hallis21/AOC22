from collections import defaultdict


distance = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) 
max_x = 4000000
max_y = 4000000
min_x = 0
min_y = 0
# x,y


with open("15.in") as f:
    lines = [[tuple(map(int, (y[2][2:-1],y[3][2:-1],y[8][2:-1],y[9][2:]))) for y in [x.strip().split(" ")]][0] for x in f.readlines()]
    
    distances = [((y[0], y[1]), distance((y[0], y[1]), (y[2], y[3]))) for y in lines]
    
    # beacons = [(x[2], x[3]) for x in lines]
    
    # create a set with all points that are in range of a sensor
    points = defaultdict(dict)

    total = 0
    for point in distances:
        print(point)
        x = 0
        
        # mark any point that is exacly the distance away from the sensor
        # a point can not have negative coordinates
        while x <= point[1]:
            y = point[1] - x
            if x + point[0][0] >= 0 and y + point[0][1] >= 0:
                points[y + point[0][1]][x + point[0][0]] = True
                total+=1
            if x + point[0][0] >= 0 and -y + point[0][1] >= 0:
                points[-y + point[0][1]][x + point[0][0]] = True
                total+=1
            if -x + point[0][0] >= 0 and y + point[0][1] >= 0:
                points[y + point[0][1]][-x + point[0][0]] = True
                total+=1
            if -x + point[0][0] >= 0 and -y + point[0][1] >= 0:
                points[-y + point[0][1]][-x + point[0][0]] = True
                total+=1
            x += 1

    # check left and right of a given point
    # the coordinates left and right of a points are "possible" if: 
    # they are not in the set, and is surrounded by points in the set
    # check up, down, left, right of the possible point
    # add to list possible if all 4 are in the set
    possible = set()
    for y in points:
        for x in points[y]:
            left_x = x - 1
            if left_x >= 0 and left_x not in points[y]:
                if left_x-1 < 0 or left_x-1 in points[y]:
                    if y-1 < 0 or left_x in points[y-1]:
                        if y+1 > max_y or left_x in points[y+1]:
                            possible.add((left_x, y))



            
    # Check all possible to see if they are in range of a sensor
    # if they are, remove them from the list
    to_remove = set()
    for point in possible:
        
        for sensor in distances:
            if distance(point, sensor[0]) < sensor[1]:
                to_remove.add(point)
                break
            if point[0] < min_x or point[0] > max_x or point[1] < min_y or point[1] > max_y:
                to_remove.add(point)

    possible = possible - to_remove

    print(total, possible)

    
    r = possible.pop()
    result = (r[0] *4000000 + r[1])
    print(result)





    exit()
    # # Draw grid, if the coordinate is in the set, print a #, otherwise print a .
    for y in range(max_y):
        for x in range(max_x):
            # mark sensors a S
            if (x, y) in [x[0] for x in distances]:
                print("S", end="")
            # mark possible with P
            elif (x, y) in possible:
                print("P", end="")
            elif x in points[y]:
                print("#", end="")
            else:
                print(".", end="")
        print()
        



        
                
