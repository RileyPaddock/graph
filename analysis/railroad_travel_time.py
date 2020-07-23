import sys
sys.path.append('src')
from tree import Tree

def modify_list(segments,start_elem):
    for i in range(len(segments)):
        if segments[i][1] == start_elem:
            segments[i] = (segments[i][1],segments[i][0])

    completion = 0
    while completion < len(segments):
        for x,y in segments:
            if x!= start_elem:
                for a,b in segments:
                    if x==b:
                        completion+=1
                        break
                else:
                    completion = 0
                    segments[segments.index((x,y))] = (segments[segments.index((x,y))][1], segments[segments.index((x,y))][0])
    return segments


def order_towns_by_travel_time_using_tree_class(starting_town,railroad_segments):
    railroad_segments = modify_list(railroad_segments,starting_town)
    map = Tree()
    map.build_from_edges(railroad_segments)
    map.breadth_first_traversal([map.root])
    return map.data

def find_num_stations(segments):
    num_stations = []
    for x,y in segments:
        if x not in num_stations:
            num_stations.append(x)
        if y not in num_stations:
            num_stations.append(y)
    return len(num_stations)

def order_towns_by_travel_time_from_scratch(starting_town, railroad_segments):
    num_stations = find_num_stations(railroad_segments)
    result = []
    queue = [starting_town]
        
    while len(result)<num_stations:
        num_connections = 0

        for i in range(len(queue)):#prints data of one layer
            num_connections = i
            if queue[i] not in result:
                result.append(queue[i])
        for i in range(len(queue)):
            for x,y in railroad_segments:
                if x == queue[i]:
                    queue.append(y)
                if y == queue[i]:
                    queue.append(x)
        #adds the next layer to the queue
        
        if len(queue) > 0:#removes the layer already printed and checks for last layer

            for i in range(num_connections + 1):
                queue.remove(queue[0])
    return result




