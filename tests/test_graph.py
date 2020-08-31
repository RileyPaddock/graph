import sys
sys.path.append('src')
from graph import Graph
edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
vertices = ['a','b','c','d','e','f']
graph = Graph(edges, vertices)
print(graph.breadth_first_search(2))