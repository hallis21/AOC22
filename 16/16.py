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
        if visited == [set('AA')]*len(tunnels_name):
            print(tunnels_name.index(neighbor))
        if neighbor not in visited[cu_i]:
            visited[cu_i].add(neighbor)
            paths.update(explore(neighbor, allowance - distance_matrix[cu_i][tunnels_name.index(neighbor)], visited, path+f",{current}"))#path + f"{current}({total_flow})->"))
            visited[cu_i].remove(neighbor)
    if not paths: return {path[1:]}
    return paths

paths = explore('AA', 30, [set()]*len(tunnels_name), "")
# Write all the paths to a file, new line seperated
# print(paths)



for path in paths:
    # split the path into two parts
    # If there is an odd number of steps, the first list will have one more element
    # If there is an even number of steps, the first list will have the same number of elements as the second list
    
    parts = [path.split(",")[i::2] for i in range(2)]
    parts[1].insert(0, "AA")

    # replace the name of the node with the distance to the previous node
    for i in range(len(parts)):
        for j in range(len(parts[i])):
            if j == 0:
                continue
    print(parts)


    




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




