# BFS REVISE
# from collections import deque
# graph = {
#     "a": ["b", "c"],
#     "b": ["d"],
#     "c": ["e"],
#     "d": ["f"],
#     "e": [],
#     "f": []
# }
# def bfs(graph, source):
#     queue = deque()
#     queue.append(source)
#     while queue:
#         node = queue.popleft()
#         print(node)
#         for neighbour in graph.get(node):
#             queue.append(neighbour)
# bfs(graph, "a")
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
def dfs(source, graph, visited_set, component_count):
    if source in visited_set:
        return
    visited_set.add(source)
    globals()[f'subgraph_{component_count}'] +=1
    for neighbour in graph.get(source):
        dfs(neighbour, graph, visited_set, component_count)


def find_components(graph):
    visited_set = set()
    component_count = 0
    components = []
    for node in graph.keys():
        if node not in visited_set:
            component_count += 1
            globals()[f'subgraph_{component_count}'] = 0
            dfs(node, graph, visited_set, component_count)
            components.append(globals()[f'subgraph_{component_count}'])
    return max(components)

print(find_components(graph))
# we can use normal count as well rather than globals and array


