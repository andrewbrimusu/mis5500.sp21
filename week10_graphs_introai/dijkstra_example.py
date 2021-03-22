import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations

import networkx as nx
from networkx.classes.function import path_weight

import matplotlib.pyplot as plt

fil = open("/home/ec2-user/environment/code/week9_graphs/zoomsession2/edges.txt")

g = nx.DiGraph()
edges = []
for line in fil.readlines():
    n1, n2, e  = line.split(",")
    e = int(e)
    edges.append((n1, n2, e))
print(edges)
g.add_weighted_edges_from(edges) 

# nx.draw(g, with_labels=True)

pos=nx.circular_layout(g) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(g,pos)
labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

plt.savefig("graph.png")

print(g.nodes)
# input()
for n1, n2 in permutations(g.nodes,2):
    print("paths from",n1,"to",n2,":")
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        print(path)
    for path in nx.all_simple_paths(g, source=n2, target=n1):
        print(path)
        
print(0)