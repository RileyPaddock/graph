import sys
sys.path.append('src')
from directed_graph import DirectedGraph

edges = [(0,1),(1,2),(3,1),(4,3),(1,4),(4,5),(3,6)]
directed_graph = DirectedGraph(edges)

print("\n Testing Children")
assert [[child.index for child in node.children] for node in directed_graph.nodes] == [[1], [2, 4], [], [1, 6], [3, 5], [], []], 'incorrect children'
print('     passed')

print('\n Testing Parents')
assert [[parent.index for parent in node.parents] for node in directed_graph.nodes] == [[], [0,3], [1], [4], [1], [4], [3]], 'incorrect parents'
print('     passed')

print('\n Testing calc_distance() pt1')
assert directed_graph.calc_distance(0,3) == 3, 'incorrect distance between (0,3)'
print('     passed')

print('\n Testing calc_distance() pt2')
assert directed_graph.calc_distance(3,5) == 3, 'incorrect distance between (3,5)'
print('     passed')

print('\n Testing calc_distance() pt3')
assert directed_graph.calc_distance(0,5) == 3, 'incorrect distance between (0,5)'
print('     passed')

print('\n Testing calc_distance() pt4')
assert directed_graph.calc_distance(4,1) == 2, 'incorrect distance between (4,1)'
print('     passed')

print('\n Testing calc_distance() pt5')
assert directed_graph.calc_distance(2,4) == False, 'incorrect distance between (2,4)'
print('     passed')

print('\n Testing calc_shortest_path() pt1')
assert directed_graph.calc_shortest_path(0,3) == [0, 1, 4, 3], 'incorrect path from (0,3)'
print('     passed')

print('\n Testing calc_shortest_path() pt2')
assert directed_graph.calc_shortest_path(3,5) == [3, 1, 4, 5], 'incorrect path from (3,5)'
print('     passed')

print('\n Testing calc_shortest_path() pt3')
assert directed_graph.calc_shortest_path(0,5) == [0, 1, 4, 5], 'incorrect path from (0,5)'
print('     passed')

print('\n Testing calc_shortest_path() pt4')
assert directed_graph.calc_shortest_path(4,1) == [4, 3, 1], 'incorrect path from (4,1)'
print('     passed')

print('\n Testing calc_shortest_path() pt5')
assert directed_graph.calc_shortest_path(2,4) == False, 'incorrect path from (2,4)'
print('     passed')
