
    
with open("i.txt", "r") as f:
    # Read lines until EOF
    cwd = {}
    cwd_top = cwd
    # skip first line
    l = f.readline()
    s = False
    while True:
        if not s: l = f.readline().strip().split()
        s = False
        if not l: break
        if l[1] == "ls":
            while True:
                l = f.readline().strip().split()
                if not l or l[0] == "$":
                    s = True
                    break
                # Add file to cwd
                if l[0] == "dir":
                    cwd[l[1]] = {"parent":cwd}
                    # cwd = cwd[l[1]]
                else:
                    cwd[l[1]] = int(l[0])
        else:
            if l[2] == "..":
                cwd = cwd["parent"]
            else:
                cwd = (cwd[l[2]])         
o = {} 
def sum_tree(d, current_path):
    o[current_path] = sum([sum_tree(v,current_path+'/'+k) for k,v in d.items() if isinstance(v,dict) and k != "parent"] + [v for k,v in d.items() if isinstance(v,int)])
    return o[current_path]
sum_tree(cwd_top, "")

needed = 30000000 - (70000000 - o[""])
print(min([v for k,v in o.items() if v >= needed]))

