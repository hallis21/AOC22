# for line in 10.in



cycle = 0
to_tick = 0
x = 1
sigs = []
v = 0
for line in [l.strip() for l in open('10.in')]:
    if "n" in line:
        to_tick = 1
    else:
        to_tick = 2
        v = int(line.split(" ")[-1])
    for t in range(to_tick):
        cycle += 1
        if (cycle-20)%40 == 0 or cycle == 20:
            sigs.append(cycle*x)
    x += v
    v = 0
    
print(sum(sigs))