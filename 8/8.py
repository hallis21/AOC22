lines = open("i.txt").readlines()
trees = []
visible = set()
view = []

for l in lines:
    trees.append([int(x) for x in l.strip()])
    view.append([[] for x in l.strip()])


# Lambda for finding the first element in a list that is larger or equal to n
int_find = lambda n, l: next((i for i, x in enumerate(l) if x >= n), False)
find = lambda n, l: int_find(n, l) if int_find(n, l) else len(l)


for i in range(0, len(trees)):
    for j in range(0, len(trees[i])):

        # Side
        left_side = trees[i][0:j]
        right_side = trees[i][j+1:]
        up = [x[j] for x in trees[0:i]]
        down = [x[j] for x in trees[i+1:]]
        
        
        # ss = *find(trees[i][j], right_side)*find(trees[i][j], up)*find(trees[i][j], down[::-1])
        
        
        s = 0
        cur = 0
        for t in left_side[::-1]:
            if t < trees[i][j]:

                cur += 1
            elif t >= trees[i][j]:

                cur += 1
                break

        s = cur
        print(cur, find(trees[i][j], left_side[::-1]))
        cur = 0
        for t in right_side:
            if t < trees[i][j]:

                cur += 1
            elif t >= trees[i][j]:

                cur += 1
                break
        s = s*cur
        print(cur, find(trees[i][j], right_side))
        cur = 0
        for t in up[::-1]:
            if t < trees[i][j]:

                cur += 1
            elif t >= trees[i][j]:

                cur += 1
                break
        s = s*cur
        print(cur, find(trees[i][j], up[::-1]))
        cur = 0
        for t in down:
            if t < trees[i][j]:

                cur += 1
            elif t >= trees[i][j]:

                cur += 1
                break
        view[i][j] = s*cur
        print(cur, find(trees[i][j], down))




print(max(map(max, view)))
