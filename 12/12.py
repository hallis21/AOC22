game_board = []

start = None
goal = None
# read 12.txt into game_board, the board should be a list of characters
# each line should be a list of characters
with open('12.txt', 'r') as f:
    for line in f:
        game_board.append(list(line.strip()))
        if 'S' in line:
            start = (len(game_board) - 1, line.index('S'))
            game_board[-1][line.index('S')] = 'a'
        if 'E' in line:
            goal = (len(game_board) - 1, line.index('E'))
            game_board[-1][line.index('E')] = 'z'
    
        game_board[-1] = [ord(char)-97 for char in game_board[-1]]


starts = lambda x: (x, start, set()) #[(i, j) for i in range(len(x)) for j in range(len(x[0])) if x[i][j] == 0])
starts2 = lambda x: [(i, j) for i in range(len(x)) for j in range(len(x[0])) if x[i][j] == 0]


# Find legal moves for a cell (i,j) in game board gb
neighbors = lambda cell, gb: [x for x in [(cell[0] - 1, cell[1]), (cell[0] + 1, cell[1]), (cell[0], cell[1] - 1), (cell[0], cell[1] + 1)] \
    if (x[0] >= 0 and x[0] < len(gb) and x[1] >= 0 and x[1] < len(gb[0])) and (gb[x[0]][x[1]] == gb[cell[0]][cell[1]] + 1\
   or gb[x[0]][x[1]] <= gb[cell[0]][cell[1]])]   

gb = starts([[ord(x)-97 if x not in ['S', 'E'] else 0 if x=='S' else 25 for x in list(line.strip())] for line in open("12.txt")])

s2 = starts2([[ord(x)-97 if x not in ['S', 'E'] else 0 if x=='S' else 25 for x in list(line.strip())] for line in open("12.txt")])





bfs = lambda cell, visited, gb, s: [(1, bfs(cell, visited+[cell], gb, s+1))[1] if s < 400 else (s+1 if gb[cell[0]][cell[1]] == 25 else 10000) for cell in neighbors(cell, gb) if cell not in visited]


flatten_nested = lambda x: [item for sublist in x for item in sublist]
recursive_flatten = lambda x: [item for sublist in x for item in (recursive_flatten(sublist) if isinstance(sublist, list) else [sublist])]


print(min([min(recursive_flatten(bfs(start_cell, [], gb[0], 1))) for start_cell in s2]))







# for each cell, check updownleftright, if legal, do recursive call
# if not legal, return 0




exit()
# print game board
print("\n".join(["".join([chr(char+97) for char in line]) for line in game_board]))
# exit()
current_step = {start}
# Add all cells that have value 0 to current_step
current_step.update([(i, j) for i in range(len(game_board)) for j in range(len(game_board[0])) if game_board[i][j] == 0])

visited = set()


steps = 0
found = False
while not found:
    if found: break
    steps+= 1
    next_step = set()
    for cell in current_step:
        # check cells up, dpwn, left, right
        for coord in [(cell[0] - 1, cell[1]), (cell[0] + 1, cell[1]), (cell[0], cell[1] - 1), (cell[0], cell[1] + 1)]:
            if coord in visited:
                continue
            if coord[0] < 0 or coord[0] >= len(game_board) or coord[1] < 0 or coord[1] >= len(game_board[0]):
                continue
            if (game_board[coord[0]][coord[1]] == game_board[cell[0]][cell[1]] + 1) or (game_board[coord[0]][coord[1]] <= game_board[cell[0]][cell[1]]):
                next_step.add(coord)
                if coord == goal:
                    found = True
                    break
                
                

            
    [visited.add(coord) for coord in current_step]
    current_step = next_step
print(steps)
        
        




# print(game_board, start, goal)