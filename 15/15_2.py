from collections import defaultdict


distance = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) 
m = 4000000

with open("15.in") as f:
    lines = [[tuple(map(int, (y[2][2:-1],y[3][2:-1],y[8][2:-1],y[9][2:]))) for y in [x.strip().split(" ")]][0] for x in f.readlines()]
    
    distances = [((y[0], y[1]), distance((y[0], y[1]), (y[2], y[3]))) for y in lines]
    
    
    # create a set with all points that are in range of a sensor
    points = defaultdict(dict)

    for point in distances:
        x = 0
        while x <= point[1]:
            y = point[1] - x
            if x + point[0][0] >= 0 and y + point[0][1] >= 0:
                points[y + point[0][1]][x + point[0][0]] = True
            if x + point[0][0] >= 0 and -y + point[0][1] >= 0:
                points[-y + point[0][1]][x + point[0][0]] = True
            if -x + point[0][0] >= 0 and y + point[0][1] >= 0:
                points[y + point[0][1]][-x + point[0][0]] = True
            if -x + point[0][0] >= 0 and -y + point[0][1] >= 0:
                points[-y + point[0][1]][-x + point[0][0]] = True
            x += 1

    possible = set()
    for y in points:
        for x in points[y]:
            left_x = x - 1
            if left_x >= 0 and left_x not in points[y]:
                if left_x-1 < 0 or left_x-1 in points[y]:
                    if y-1 < 0 or left_x in points[y-1]:
                        if y+1 > m or left_x in points[y+1]:
                            possible.add((left_x, y))

    to_remove = set()
    for point in possible:
        
        for sensor in distances:
            if distance(point, sensor[0]) < sensor[1]:
                to_remove.add(point)
                break
            if point[0] < 0 or point[0] > m or point[1] < 0 or point[1] > m:
                to_remove.add(point)

    possible = possible - to_remove
    
    r = possible.pop()
    result = (r[0] *4000000 + r[1])
    print(result)
