graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
    "n": ["o"]
}

# Logic:
# We choose an element in graph, push it to stack. 
# See if the stack is empty. If not, then pop , print and then push its neighbour to the stack.
# If stack is not empty, repeat the process.
# Problem with this approach is, if there is a sub graph that is disconnected from rest fo the graph, 
# that wll remain unvisited. See above graph , n:["o"] will remain unvisited.
visited = []
def depth_first_traversal(graph, source):
    stack = []
    # stack.append(list(graph.keys())[0])
    stack.append(source)
    # res = []
    while stack:
        top = stack.pop()
        print(top)
        visited.append(top)
        if not graph.get(top):
            continue
        for neighbour in graph.get(top):
            stack.append(neighbour)
        
# To solve the above problem , let's maintain if a node is visited or not.

def dfs_all_nodes(graph):
    for source in graph.keys():
        if source not in visited:
            depth_first_traversal(graph, source)

def depth_first_traversal_recursive(graph, source):
    print(source)
    for neighbour in graph.get(source):
        print("working on",source)
        depth_first_traversal_recursive(graph, neighbour)

# dfs_all_nodes(graph)
# x = list(graph.keys())[0]
# print(x)
depth_first_traversal_recursive(graph, "a")