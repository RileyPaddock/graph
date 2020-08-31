import sys
sys.path.append('src')
from node import Node
class Graph:
    def __init__(self, edges, verticies):
        self.edges = edges
        self.verticies = verticies
        self.nodes = [Node(i) for i in range(len(verticies))]
        self.set_up_nodes()

    def set_up_nodes(self):
        for i in range(len(self.nodes)):
            self.nodes[i].set_value(self.verticies[i])
        for x,y in self.edges:
            self.nodes[x].set_neighbor(self.nodes[y])

    def depth_first_search(self,starting_index):
        result = [starting_index]
        i = starting_index
        while len(result)<len(self.nodes):
            for node in self.nodes[i].neighbors:
                if node.index not in result:
                    result.append(node.index)
                    i = node.index
        return result
        
    def breadth_first_search(self,starting_index):
        result = []
        queue = [starting_index]
        while len(result) < len(self.nodes):
                for neighbor in self.nodes[queue[0]].neighbors:
                    queue.append(neighbor.index)
                if queue[0] not in result:
                    result.append(queue[0])
                queue.remove(queue[0])
        return result

    def find_distance(self,i,j):
        result = []
        queue = [i]
        generation = 0
        while len(result) < len(self.nodes):
            if self.nodes[j].index in queue:
                return generation
            static_len = len(queue)
            for i in range(static_len):
                for neighbor in self.nodes[queue[0]].neighbors:
                    queue.append(neighbor.index)
                if queue[0] not in result:
                    result.append(queue[0])
                queue.remove(queue[0])
            generation += 1


edges = [(0,1),(1,2),(1,3),(3,4),(1,4),(4,5)]
vertices = ['a','b','c','d','e','f']
graph = Graph(edges,vertices)

print(graph.find_distance(0,4))
#2
print(graph.find_distance(5,2))
#3
print(graph.find_distance(0,5))
#3
print(graph.find_distance(4,1))
#1
print(graph.find_distance(3,3))
#0

    