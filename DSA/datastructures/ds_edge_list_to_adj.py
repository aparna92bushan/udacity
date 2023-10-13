# Given an undirected path, find out whether there is a path between two nodes.
# Since it is easy to do traversals in adjacency list, we first convert the edge list to adjacency list and 
# then do the traversal
# But catch is that there can be cycles leaving u in infinite loops in undirected graphs especially
edge_list = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]
# {
#   'i': ['j', 'k'], 
#   'j': ['i'], 
#   'k': ['i', 'm', 'l'], 
#   'm': ['k'], 
#   'l': ['k'], 
#   'o': ['n'], 
#   'n': ['o']
# }

# convert above edge list to adjacency list
# def convert_edge_list_to_adj_list(main_edge_list):
#     graph = {}
#     for edge_list in main_edge_list:
#         if edge_list[0] not in graph.keys():
#             graph[edge_list[0]] = []
#         if edge_list[1] not in graph.keys():
#             graph[edge_list[1]] = []
#         graph[edge_list[0]].append(edge_list[1])
#         graph[edge_list[1]].append(edge_list[0])
#     return graph

# def graph_has_path(graph, source, dest, visited_set):
#     if source == dest:
#         return True
#     if source in visited_set:
#         return
#     visited_set.add(source)
#     for neighbour in graph.get(source):
#         if graph_has_path(graph, neighbour, dest, visited_set) == True:
#             return True
#     return False

# def find_if_path(edge_list, nodeA, nodeB):
#     adjacency_list = convert_edge_list_to_adj_list(edge_list)
#     visited_set = set()
#     return graph_has_path(adjacency_list, nodeA, nodeB, visited_set)
            
def convert_edge_list_to_adj_list(edge_list):
    adj_graph = {}
    for edge in edge_list:
        if edge[0] not in adj_graph.keys():
            adj_graph[edge[0]] = []
        if edge[1] not in adj_graph.keys():
            adj_graph[edge[1]] = []
        adj_graph[edge[0]].append(edge[1])
        adj_graph[edge[1]].append(edge[0])
    return adj_graph

def find_if_path(src, dest, graph, visited_set):
    if not graph.get(src) or not graph.get(dest):
        return False
    if src == dest:
        return True
    if src in visited_set:
        return
    visited_set.add(src)
    for neighbour in graph[src]:
        if find_if_path(neighbour, dest, graph, visited_set) == True:
            return True
    return False

def graph_has_path(src, dest, edge_list):
    visited_set = set()
    adj_list = convert_edge_list_to_adj_list(edge_list)
    # for node in adj_list.keys(): Not necessary because if disconnected means there isn't a path anyway but in traversal, we should do this
    #     if node not in visited_set:
    return find_if_path(src, dest, adj_list, visited_set)
print(graph_has_path("a", "o", edge_list))