
knot_pos = [[0,0] for i in range(10)]
movements = [[] for i in range(10)]
def update_knots():
    for i in range(1,10):
        if abs(knot_pos[i][1] - knot_pos[i-1][1]) > 1:
            knot_pos[i][1] -= 1
            if knot_pos[i][1] < knot_pos[i-1][1]:
                knot_pos[i][1] += 2

            if knot_pos[i][0] < knot_pos[i-1][0]:
                knot_pos[i][0] += 1
            elif knot_pos[i][0] > knot_pos[i-1][0]:
                knot_pos[i][0] -= 1
        elif abs(knot_pos[i][0] - knot_pos[i-1][0]) > 1:
            knot_pos[i][0] -= 1
            if knot_pos[i][0] < knot_pos[i-1][0]:
                knot_pos[i][0] += 2

            if knot_pos[i][1] < knot_pos[i-1][1]:
                knot_pos[i][1] += 1
            elif knot_pos[i][1] > knot_pos[i-1][1]:
                knot_pos[i][1] -= 1
    movements[i].append(tuple(x for x in knot_pos[i]))

for line in open("9.in"):
    if line[0] == "R":
        for i in range(int(line[1:])):
            knot_pos[0] = (knot_pos[0][0], knot_pos[0][1]+1)
            movements[0].append(knot_pos[0])
            update_knots()
    elif line[0] == "L":
        for i in range(int(line[1:])):
            knot_pos[0] = (knot_pos[0][0], knot_pos[0][1]-1)
            movements[0].append(knot_pos[0])
            update_knots()
    elif line[0] == "U":
        for i in range(int(line[1:])):
            knot_pos[0] = (knot_pos[0][0]+1, knot_pos[0][1])
            movements[0].append(knot_pos[0])
            update_knots()
    elif line[0] == "D":
        for i in range(int(line[1:])):
            knot_pos[0] = (knot_pos[0][0]-1, knot_pos[0][1])
            movements[0].append(knot_pos[0])
            update_knots()
        
print(len(set(movements[9])))