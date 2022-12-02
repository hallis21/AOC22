with open("inp.txt", "r") as f:
    lines = f.readlines()
    
    
    # Sum all lines in the file, they are int
    # If a blank line appears in the file, add the sum to a list and start over
    s = 0
    el = []
    biggest = 0
    big_index = 0
    i = 0
    for line in lines:
        if line == "\n":
            el.append(s)
            if s > biggest:
                biggest = s
                big_index = i
            i += 1
            s = 0
        else:
            s += int(line.strip())
    el.sort()
    # print(el[-1]+el[-2]+el[-3])
            
            
