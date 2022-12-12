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
                
    print(steps)
                

            
    [visited.add(coord) for coord in current_step]
    current_step = next_step
print(steps)
        
        




# print(game_board, start, goal)