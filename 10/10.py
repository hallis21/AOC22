cycle = 0
x = 1
ss = 0
left_pos = 0
to_print = ""


def draw_pixle():
    global to_print, left_pos
    if left_pos >= 40: 
        left_pos = 0
        to_print+= "\n"
    left_pos += 1
    to_print += "#" if left_pos in range(x-1, x+2) else "."
        
        
for l in open("10.in"):
    b = l.split(" ")
    cycle += 1

        
    draw_pixle()
    if cycle == 20 or (cycle-20) % 40 == 0:
        ss += cycle*x
    
    if b[0] == "addx":
        cycle += 1
        if cycle == 20 or (cycle-20) % 40 == 0:
            ss += cycle*x
        x += int(b[1])
        draw_pixle()
    
    
    
print(to_print)