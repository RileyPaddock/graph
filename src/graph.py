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

    def calc_distance(self,i,j):
        result = []
        queue = [i]
        generation = 0
        while self.nodes[j].index not in queue:
            static_len = len(queue)
            for i in range(static_len):
                for neighbor in self.nodes[queue[0]].neighbors:
                    queue.append(neighbor.index)
                if queue[0] not in result:
                    result.append(queue[0])
                queue.remove(queue[0])
            generation += 1
        return generation

    def calc_shortest_path(self,start, end):
        self.nodes[start].previous = "done"
        result = [end]
        queue = [start]
        while end not in queue:
            for neighbor in self.nodes[queue[0]].neighbors:
                if self.nodes[neighbor.index].previous is None:
                    self.nodes[neighbor.index].previous = queue[0]
                queue.append(neighbor.index)
            queue.remove(queue[0])

        active_node = self.nodes[end]
        while active_node.previous != "done":
            result.append(active_node.previous)
            active_node = self.nodes[active_node.previous]

        result.reverse()
        for node in self.nodes:
            node.previous = None
        return result

