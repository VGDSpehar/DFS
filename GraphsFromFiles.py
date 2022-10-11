import os

class Graphs:
    graphs = []

    def __init__(self):
        files = os.listdir('graphs/')
        for file in files :
            with open("graphs/"+file) as f:
                graph = {}
                node = 1
                lines = f.readlines()
                for line in lines:
                    graph[str(node)] = line.split()
                    node += 1
            self.graphs.append(graph)
    
    def printG(): 
        print(Graphs.graphs)

    def printGraphs():
        for graph in Graphs.graphs:
            nodes = graph.keys()
            for node in nodes:
                line = node + " : "
                neighbours = graph[node]
                for neighbour in neighbours:
                    line += neighbour + " "
                print(line)
