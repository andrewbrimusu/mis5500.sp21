import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations
from itertools import combinations

import networkx as nx
from networkx.classes.function import path_weight

import matplotlib.pyplot as plt


# rates = [
#     [1, 0.23, 0.25, 16.43, 18.21, 4.94],
#     [4.34, 1, 1.11, 71.40, 79.09, 21.44],
#     [3.93, 0.90, 1, 64.52, 71.48, 19.37],
#     [0.061, 0.014, 0.015, 1, 1.11, 0.30],
#     [0.055, 0.013, 0.014, 0.90, 1, 0.27],
#     [0.20, 0.047, 0.052, 3.33, 3.69, 1],
# ]

# currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')

# g = nx.DiGraph()
# edges = []
# i = 0
# for c1 in currencies:
#     j = 0
#     for c2 in currencies:
#         if c1 != c2:
#             edges.append((c1, c2, rates[i][j]))
#             print("adding edge: ", c1, c2, rates[i][j])
#         j +=1
#     i += 1
# g.add_weighted_edges_from(edges) 
# # print(g.info())

# print(g.nodes)
# # input()
# for n1, n2 in permutations(g.nodes,2):
#     print("paths from ", n1, "to", n2, "----------------------------------")
#     for path in nx.all_simple_paths(g, source=n1, target=n2):
#         print(path)
#     for path in nx.all_simple_paths(g, source=n2, target=n1):
#         print(path)
        
# print(0)


import requests
import json

currencies = ["usd", "eur", "gbp", "mxn", "rub", "inr"]

g = nx.DiGraph()
edges = []

url1 = "http://www.floatrates.com/daily/"
url2 = ".json"
for c1, c2 in permutations(currencies,2):
    url = url1 + c1 + url2
    # add logic to get currency information
    
g.add_weighted_edges_from(edges) 


pos=nx.circular_layout(g) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(g,pos)
labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

plt.savefig("currency_graph.png")


