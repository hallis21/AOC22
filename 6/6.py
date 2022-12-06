
# print([[i for i in range(len(l)) if len(set(l[i-14:i])) == 14 and (print(i) or exit())] for l in [open("i.txt").read()]])


# print(open("i.txt").read())


print(next(i for d in open("i") for i in range(len(d))if len(set(d[i-4:i]))>3))