import sys
sys.path.append('src')
from graph import Graph
edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
vertices = ['a','b','c','d','e','f']
graph = Graph(edges, vertices)

print(graph.calc_shortest_path(0,4))
#[0, 1, 4]
print(graph.calc_shortest_path(5,2))
#[5, 4, 1, 2]
print(graph.calc_shortest_path(0,5))
#[0, 1, 4, 5]
print(graph.calc_shortest_path(4,1))
#[4, 1]
print(graph.calc_shortest_path(3,3))
#[3]