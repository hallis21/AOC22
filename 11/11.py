

lines = open('11.in').readlines()
    
monkeys = []
mi = 0
li = 0
dividoos = 1

while li < len(lines):
    b = lines[li].split()
    if b and b[0] == "Monkey":
        monkeys.append({"items": [int(x.replace(",", "")) for x in lines[li+1].split()[2:]],\
            "op": lines[li+2][13:-1], \
            "test": int(lines[li+3][21:-1]), \
            "true": int(lines[li+4].strip()[25:]), \
            "false": int(lines[li+5].strip()[26:]),
            "inspected":0})
        dividoos *= monkeys[-1]["test"]
        li += 4        
    li += 1

for n in range(10000):
    for mi, monkey in enumerate(monkeys):
        for i, item in enumerate(monkey["items"]) :
            # inspecting    
            in_dict = {"old":monkey["items"][i]}
            
            exec(monkey["op"], in_dict)
            monkey["items"][i] = in_dict["new"]
            # monkey["items"][i] = monkey["items"][i]//3
            # Test
            
            new_worry = monkey["items"][i] % dividoos
            
            if (monkey["items"][i] % monkey["test"]) == 0:
                # True
                monkeys[monkey["true"]]["items"].append(new_worry)
                # print(f"Passed from {mi} to {monkey['true']}")
            else:
                monkeys[monkey["false"]]["items"].append(new_worry)
                # print(f"Passed from {mi} to {monkey['false']}")
            monkey["inspected"] += 1
                
        monkey["items"] = []
        
# print inspected
print([monkey["inspected"] for monkey in monkeys])
# FInd the top two inspected and multiply them
print(max([monkey["inspected"] for monkey in monkeys]) * max([monkey["inspected"] for monkey in monkeys if monkey["inspected"] != max([monkey["inspected"] for monkey in monkeys])]))