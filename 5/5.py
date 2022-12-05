# with open("i.txt", "r") as f:
#     lines = f.read().split("\n")
#     i = 0
#     num_stacks = (len(lines[0])//4) +1
#     stacks = [[] for i in range(num_stacks)]

#     while lines[i][1 ] != "1":
#         for j in range(num_stacks):
#             s = lines[i][j*4:(j+1)*4].strip()
#             if s:
#                 stacks[j].append(s)
#         i += 1
#     i+=2
#     stacks = [x[::-1] for x in stacks]
#     while i < len(lines):
        
#         b= lines[i].split(" ")
#         mv_n = int(b[1])
#         mv_from = int(b[3])
#         mv_to = int(b[5])
#         # Part one
#         # for n in range(mv_n):
#         #     stacks[mv_to-1].append(stacks[mv_from-1].pop())

#         # Part two
#         # Move all elemets at once instead of one by one
#         stacks[mv_to-1].extend(stacks[mv_from-1][-mv_n:])
#         stacks[mv_from-1] = stacks[mv_from-1][:-mv_n]
#         i+=1
#     print("".join([x[-1] for x in stacks]).replace("[","").replace("]",""))



# Make the previous into a single list comprehension

# if pos0 != "" then add to list

# command is a list of 3 elements [num, from, to]

parse_cmd = lambda cmd, stacks: [[stacks[cmd[2]-1].extend(stacks[cmd[1]-1][-cmd[0]:])], [stacks[cmd[1]-1].pop() for _ in range(cmd[0])]]


fill = lambda e: [[[e[2][n].append((l[0][n*4:(n+1)*4-1])) for l in e[0] if l[0] and l[0][n*4:(n+1)*4].strip()] for n in range(e[1])],
                  [e[2][n].reverse() for n in range(e[1])],
                  [parse_cmd(list(map(int, cmd[1].split(" ")[1::2])), e[2]) for cmd in e[0] if cmd[1] and len(cmd[1].split(" ")) == 6], 
                  e][3]


print("".join([l.pop() for l in 
    list(map(lambda e: [[[e[2][n].append((l[0][n*4:(n+1)*4-1])) for l in e[0] if l[0] and l[0][n*4:(n+1)*4].strip()] for n in range(e[1])],[e[2][n].reverse() for n in range(e[1])],[(lambda cmd, stacks: [[stacks[cmd[2]-1].extend(stacks[cmd[1]-1][-cmd[0]:])], [stacks[cmd[1]-1].pop() for _ in range(cmd[0])]])(list(map(int, cmd[1].split(" ")[1::2])), e[2]) for cmd in e[0] if cmd[1] and len(cmd[1].split(" ")) == 6], e][3], [(a1, len(a1[0][0])//4+1, [[] for x in range(len(a1[0][0])//4+1)]) for a1 in [[(a,b) for a,b in [("".join([y for y in x if "[" in x])[:-1],"".join([y for y in x if "[" not in x])[:-1]) for x in open("i.txt").readlines()]]]]))[0][2]]).replace("[","").replace("]",""))