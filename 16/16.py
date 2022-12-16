import itertools
from math import factorial


valves = [[(y[1],int(y[4].replace("rate=", "")[:-1]),[z.replace(",", "") for z in y[9:]]) for y in [x.strip().split(' ')]][0] for x in open('16.in').readlines()]

class Tunnel:
    def __init__(self, name, flowrate, neighbors, map) -> None:
        self.name = name
        self.flowrate = flowrate
        # list of all names of neighbors
        self.neighbors = neighbors
        # A dict of all the tunnels in the map, by name
        self.map = map


# It costs 1 unit of time to move from one tunnel to another
# It costs 1 unit of time to open any given valve
# Once a valve is open, it stays open, and will accumulate "flow" per unit of time
# The flowrate of a tunnel is the amount of flow that will be added to the valve
# Find the best path to take so that the flowrate will be maximized after 30 units of time
# We start at name "AA", there is no point opening valves that have 0 flowrate

# Compute all paths that visit every tunnel with flowrate > 0
# We can visit a tunne twice
# We can visit a tunnel with flowrate 0
# We can visit a tunnel with flowrate 0, but we can't open it
# There should be no cycles


# Create a dict of all the tunnels
tunnels = {x[0]:Tunnel(x[0], x[1], x[2], valves) for x in valves}


# List of all the tunnels that have flowrate > 0
tunnels_with_flowrate = [x for x in tunnels.values() if x.flowrate > 0 or x.name == "AA"]
tunnels_name = [x.name for x in tunnels.values() if x.flowrate > 0 or x.name == "AA"]

# Create a distance matrix between the tunnels with flowrate > 0
# The distance between two tunnels is the number of tunnels between them

distance_matrix = [[0 for x in tunnels_with_flowrate] for y in tunnels_with_flowrate]

for i in range(len(tunnels_with_flowrate)):
    for j in range(len(tunnels_with_flowrate)):
        if i == j:
            distance_matrix[i][j] = 0
        else:
            # BFS
            visited = set()
            queue = [(tunnels_with_flowrate[i], 0)]
            while queue:
                current, distance = queue.pop(0)
                if current.name == tunnels_with_flowrate[j].name:
                    distance_matrix[i][j] = distance
                    break
                if current.name not in visited:
                    visited.add(current.name)
                    for neighbor in current.neighbors:
                        queue.append((tunnels[neighbor], distance + 1))



# set any edge greater tham 10 to 0
# for i in range(len(distance_matrix)):
#     for j in range(len(distance_matrix)):
#         if distance_matrix[i][j] > 10:
#             distance_matrix[i][j] = 0



# paths = explore('AA', 30, set())
def explore(current, allowance, visited, path):
    # print(current, allowance, visited, path)
    paths = set()
    

    if current != 'AA':
        allowance -= 1
    
    total_flow = allowance * tunnels[current].flowrate
    if allowance <= 0:
        return {path[1:]}


    # Use one allowance to open the valve
    # print(current, allowance, tunnels[current].flowrate, total_flow)
    # print(current.name, allowance, visited)
    cu_i = tunnels_name.index(current)
    for neighbor in [x for x in tunnels_name if distance_matrix[cu_i][tunnels_name.index(x)] > 0]:
        if current == 'AA' and visited == [set()]*len(tunnels_name):
            print(neighbor)
        if neighbor not in visited[cu_i]:
            visited[cu_i].add(neighbor)
            paths.update(explore(neighbor, allowance - distance_matrix[cu_i][tunnels_name.index(neighbor)], visited, path+f",{current}"))#path + f"{current}({total_flow})->"))
            visited[cu_i].remove(neighbor)
    if not paths: return {path[1:]}
    return paths

paths = explore('AA', 35, [set()]*len(tunnels_name), "")

# Find the max length of the paths
# split on ","
print("Finding max length...")
print(max([len(x.split(",")) for x in paths]))

exit()
# Write all the paths to a file, new line seperated
# print(paths)

print("Exploring paths...")
all_total = []
for i, path in enumerate(paths):
    if i % 1000000: print(f"{i}/\n{len(paths)}")
    # split the path into two parts
    # If there is an odd number of steps, the first list will have one more element
    # If there is an even number of steps, the first list will have the same number of elements as the second list
    
    parts = [path.split(",")[i::2] for i in range(2)]
    parts[1].insert(0, "AA")

    # replace the name of the node with the distance to the previous node, and flowrate
    new_parts = [[], []]
    for i in range(len(parts)):
        for j in range(len(parts[i])):
            if j == 0:
                new_parts[i].append((0, 0))
                continue
            new_parts[i].append((distance_matrix[tunnels_name.index(parts[i][j-1])][tunnels_name.index(parts[i][j])], tunnels[parts[i][j]].flowrate))
    
    
    # print(parts)
    # Check if part is l
    # l = [['AA', 'JJ', 'BB', 'CC'], ['AA', 'DD', 'HH', 'EE']]
    # pog = False
    # if parts[0] == l[0] and parts[1] == l[1]:
    #     pog = True   

    totals = [[], []]
    times = [[], []]
    for i in range(len(new_parts)):
        allowance = 26
        for j in range(len(new_parts[i])):
            allowance -= new_parts[i][j][0]+1
            totals[i].append(new_parts[i][j][1])
            times[i].append(allowance)
    # if pog: 
    #     print(parts, totals)

    current = 0
    total = 0
    for t in range(1, 27):
        if 26-t in times[0]:
            current += totals[0][times[0].index(26-t)]
        if 26-t in times[1]:
            current += totals[1][times[1].index(26-t)]
        total += current
    all_total.append(total)
print()
print(max(all_total))




# sums = []
# for p in paths:
#     nums = [int(x) for x in p.split(",")]
#     sums.append(sum(nums))

# print(max(sums))
exit(0)
with open('16.out', 'w') as f:
    for path in paths:
        f.write(path + "\n")




exit(0)

# Plot the graph of all the tunnels with flowrate > 0
# Add the distance between each tunnel as a label

# using matplotlib
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_nodes_from([x.name for x in tunnels_with_flowrate])
for i in range(len(tunnels_with_flowrate)):
    for j in range(len(tunnels_with_flowrate)):
        if distance_matrix[i][j] > 0:
            G.add_edge(tunnels_with_flowrate[i].name, tunnels_with_flowrate[j].name, weight=distance_matrix[i][j])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=6)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.axis('off')
plt.show()




