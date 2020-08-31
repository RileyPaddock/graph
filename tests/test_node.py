from node import Node

string_node = Node(0)
print(string_node.index)
#0
string_node.set_value('asdf')
print(string_node.value)
#'asdf'
print(string_node.neighbors)
#[]
 
numeric_node = Node(1)
numeric_node.set_value(765)
numeric_node.set_neighbor(string_node)
print(numeric_node.neighbors[0].value)
#'asdf'
print(string_node.neighbors[0].value)
#765
 
array_node = Node(2)
array_node.set_value([[1,2],[3,4]])
array_node.set_neighbor(numeric_node)
print(array_node.neighbors[0].value)
#765
print(numeric_node.neighbors[1].value)
#[[1,2],[3,4]]