
knot_pos = [(0,0) for i in range(10)]
last_pos = [(0,0) for i in range(10)]

movements = []
distance = lambda head, tail: 1 if abs(head[0]-tail[0]) == 1 and abs(head[1]-tail[1]) == 1 else abs(head[0]-tail[0]) + abs(head[1]-tail[1]) 

for line in open("9.in"):
    if line[0] == "R":
        for i in range(int(line[1:])):
            knot_pos[0] = (knot_pos[0][0], knot_pos[0][1]+1)
            movements.append(knot_pos[0])
    elif line[0] == "L":
        for i in range(int(line[1:])):
            knot_pos[0] = (knot_pos[0][0], knot_pos[0][1]-1)
            movements.append(knot_pos[0])
    elif line[0] == "U":
        for i in range(int(line[1:])):
            knot_pos[0] = (knot_pos[0][0]+1, knot_pos[0][1])
            movements.append(knot_pos[0])
    elif line[0] == "D":
        for i in range(int(line[1:])):
            knot_pos[0] = (knot_pos[0][0]-1, knot_pos[0][1])
            movements.append(knot_pos[0])
    

    for i in range(1,2):
        delta_pos = (knot_pos[i][0]-last_pos[i-1][0], knot_pos[i][1]-last_pos[i-1][1])
        last_pos[i-1] = knot_pos[i-1]
        if distance(knot_pos[i], knot_pos[i-1]) > 1:
            knot_pos[i] = (knot_pos[i-1][0]-delta_pos[0], knot_pos[i-1][1]-delta_pos[1])
    print(knot_pos[0])
            # last_pos[i] = knot_pos[i]
        # else: break
        
        
        
        

print(knot_pos[1])
# def sim_knot(new_movement, knot_i)


# Get the distance between two points, if they are diagonal, it should return 1



    
print()
tail_pos = (0,0)
tail_movements = [(0,0)]
last_head_pos = (0,0)

for m in movements:
    delta_pos = (m[0]-last_head_pos[0], m[1]-last_head_pos[1])
    last_head_pos = m
    # print(m, delta_pos, tail_pos, distance(tail_pos, m))
    if distance(tail_pos, m) > 1:
        tail_movements.append((m[0]-delta_pos[0], m[1]-delta_pos[1]))
        tail_pos = (m[0]-delta_pos[0], m[1]-delta_pos[1])
        print(tail_pos)
        # print("\n")
print(tail_pos)

# [print(x) for x in tail_movements]
# print_grid(set(tail_movements), min(x[0] for x in tail_movements)-25,max(x[0] for x in tail_movements)+25, min(x[1] for x in tail_movements)-25,max(x[1] for x in tail_movements)+25)

print(len(set(tail_movements)))
