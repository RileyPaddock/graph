class WeightedGraph:
    def __init__(self, weights):
        self.weights = weights
        self.dvalues = {x:99999 for x in list(set([x for x,y in self.weights]+[y for x,y in self.weights]))}


    def calc_dvalues(self,current, queue = [],visited = [], start = True):
        if start == True: 
            self.dvalues[current] = 0 
            queue.append(current)

        for x,y in self.weights:
            if x == current:
                if self.dvalues[x]+self.weights[(x,y)] < self.dvalues[y]:
                    self.dvalues[y] = self.dvalues[x]+self.weights[(x,y)]
            elif y == current:
                if self.dvalues[y]+self.weights[(x,y)] < self.dvalues[x]:
                    self.dvalues[x] = self.dvalues[y]+self.weights[(x,y)]
        visited.append(current)
        queue.remove(current)

        if len(visited) == len(list(set([x for x,y in self.weights]+[y for x,y in self.weights]))):
            return
        else:
            connected_dvalues = [y for x,y in self.weights if x == current and y not in visited]+[x for x,y in self.weights if y == current and x not in visited]

            for neighbors in connected_dvalues:
                queue.append(neighbors)
            if connected_dvalues != []:
                return self.calc_dvalues(min([(self.dvalues[x],x) for x in connected_dvalues])[1],queue, visited, False)
            else:
                return self.calc_dvalues(queue[0],queue, visited, False)

    def calc_distance(self,start, end):
        self.dvalues = {x:99999 for x in list(set([x for x,y in self.weights]+[y for x,y in self.weights]))}
        self.calc_dvalues(start, [],[],True)
        return self.dvalues[end]
        
    def calc_shortest_path(self, start, end):
        self.calc_dvalues(start, [], [], True)
        current = start
        path = [start]
        while current != end:
            neighbors = [y for x,y in self.weights if x == current and y not in path]+[x for x,y in self.weights if y == current and x not in path]
            dvalues = [self.dvalues[x] for x in neighbors]
            best_move = neighbors[dvalues.index(min(dvalues))]
            path.append(best_move)
            current = best_move
        return path


weights = {
    (0,1): 3,
    (1,7): 4,
    (7,2): 2,
    (2,5): 1,
    (5,6): 8,
    (0,3): 2,
    (3,2): 6,
    (3,4): 1,
    (4,8): 8,
    (8,0): 4
}

weighted_graph = WeightedGraph(weights)
shortest_path = weighted_graph.calc_shortest_path(8,4)
print(shortest_path)
#[8, 0, 3, 4]


print(weighted_graph.calc_distance(8,4))
#7

print([weighted_graph.calc_distance(8,n) for n in range(9)])
#[4, 7, 12, 6, 7, 13, 21, 11, 0]