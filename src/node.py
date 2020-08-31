class Node:
    def __init__(self,index):
        self.index = index
        self.value = None
        self.neighbors = []

    def set_value(self,new_value):
        self.value = new_value

    def set_neighbor(self,node):
        self.neighbors.append(node)
        node.neighbors.append(self)

