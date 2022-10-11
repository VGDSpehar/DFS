from GraphsFromFiles import *
from DFS import *
import random

graphs = Graphs()
for graph in graphs.graphs:
    print("Graphe : ")
    print(graph)
    DFS.printResult(DFS.dfs(graph, input("noeud de départ :")))