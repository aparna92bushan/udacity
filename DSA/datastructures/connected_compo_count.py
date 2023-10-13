# find out the number of components in a graph
# graph = {
#   'i': ['j', 'k'], 
#   'j': ['i'], 
#   'k': ['i', 'm', 'l'], 
#   'm': ['k'], 
#   'l': ['k'], 
#   'o': ['n'], 
#   'n': ['o']
# }
graph = {
    3: [],
    4: [6],
    6: [4,5,7,8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}
def dfs(source, graph, visited_set):
    if source in visited_set:
        return
    visited_set.add(source)
    for neighbour in graph.get(source):
        dfs(neighbour, graph, visited_set)

def find_components(graph):
    visited_set = set()
    component_count = 0
    for node in graph.keys():
        if node not in visited_set:
            component_count += 1
            dfs(node, graph, visited_set)
    return component_count

print(find_components(graph))