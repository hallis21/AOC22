


print(sum([1 for l in [[set(range(int(x),int(y)+1)) for x,y in [s.split(",")[0].split("-")]][0].\
    intersection([set(range(int(x),int(y)+1)) for x,y in [s.split(",")[1].split("-")]][0]) for s in open("i.txt").read().split("\n")] if l]))
 
 


exit()
res = 0
for l in open("i.txt"):
    l = l.strip()
    first, second = l.split(",")
    
    
    print([set(range(int(x),int(y)+1)) for x,y in [first.split("-")]][0].\
        intersection([set(range(int(x),int(y)+1)) for x,y in [second.split("-")]][0]))
    
    # pairs = ([int(x) for x in first.split("-")], [int(x) for x in second.split("-")])

    
    # if pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][1]:
    #     res += 1
    # elif pairs[0][0] >= pairs[1][0] and pairs[0][1] <= pairs[1][1]:
    #     res += 1
    
print(res)