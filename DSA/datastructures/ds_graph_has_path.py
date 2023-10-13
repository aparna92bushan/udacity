# Given a directed graph, determine whether there is a path between two given nodes (S and D)
from collections import deque
graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

def has_path_depth_first_approach(graph, source, destination):
    if source == destination:
        return True
    for neighbour in graph.get(source):
        if has_path_depth_first_approach(graph, neighbour, destination) == True:
            return True
    return False

# print(has_path_depth_first_approach(graph, "f", "j"))
# print(has_path_depth_first_approach(graph, "i", "h"))

def has_path_breadth_first(graph, source, destination):
    queue = deque()
    queue.append(source)
    while queue:
        first = queue.popleft()
        if first == destination:
            return True
        for e in graph.get(first):
            queue.append(e)
    return False

print(has_path_breadth_first(graph, "f", "j"))
print(has_path_breadth_first(graph, "i", "h"))