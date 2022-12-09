

# (lambda x, l: [True if y >= x else False for y in l ]) = 
# # Find the index of the first true value in a list
# (lambda l: l.index(True)+1 if True in l else len(l)) = 


# get_best_score = 




print((lambda l: max([max([\
    (lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(l[i][j], [l[k][j] for k in range(i)][::-1]))*\
    (lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(l[i][j], [l[k][j] for k in range(i+1, len(l))]))* \
    (lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(l[i][j], l[i][:j][::-1]))*\
    (lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(l[i][j], l[i][j+1:])) \
    for j in range(len(l[i]))]) for i in range(len(l))]))([[int(y) for y in x.strip()] for x in open("8.in")]))
exit()
scores = []
for i in range(len(ll)):
    for j in range(len(ll[i])):
        # all items same coulum above row

        score = (lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(ll[i][j], [ll[k][j] for k in range(i)][::-1]))*\
        (lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(ll[i][j], [ll[k][j] for k in range(i+1, len(ll))]))*\
        (lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(ll[i][j], ll[i][:j][::-1]))*\
        (lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(ll[i][j], ll[i][j+1:]))

        scores.append(score)
print(max(scores))
# print((lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(1, [1, 1, 3, 4, 5])))

# print((lambda l: l.index(True)+1 if True in l else len(l))((lambda x, l: [True if y >= x else False for y in l ])(3, [2, 3, 3, 1, 4, 2])))

# print()
