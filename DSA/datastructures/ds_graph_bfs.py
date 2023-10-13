# logic:
# start at a node. put its neighbours in a queue. Remove first entered element from queue.
# when removing, print and put its neighbours in queue and repeat.

from collections import deque
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def breadth_first_traversal(graph):
    queue = deque()
    queue.append(list(graph.keys())[0])
    while queue:
        first = queue.popleft()
        print(first)
        for e in graph.get(first):
            queue.append(e)

# breadth_first_traversal_recursive(graph, source): can't be really done since we want to loop over all the elements in list value for a key
# can be done only iteratively. As recursive stack will kinda compete against the queue
breadth_first_traversal(graph)