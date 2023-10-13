# 2. Array based:-
#     This is based on BFS traversal i,e level order. 
#     if root is at arr[0], then 
#         left child index    = 2*0 + 1
#         right child index   = 2*0 + 2

#         so 2*n + 1  and 2*n + 2 are the children of a node at position n 

class BinTree:
    def __init__(self, root) -> None:
        self.root = root
        self.arr = [None]*20
        self.arr[0] = self.root

    def insert_left(self, child, parent):
        # When you know the parent, but if we know the index, we can use it directly.
        count = 0
        for el in self.arr:
            if el == parent:
                self.arr.insert(2*count + 1, child)
                return
            count += 1
        raise ValueError("No such element found in tree:- ", parent)
    def insert_right(self, child, parent):
        count = 0
        for el in self.arr:
            if el == parent:
                self.arr.insert(2*count+2, child)
                return
            count += 1
        return ValueError("No such element found in tree:-", parent)
# say the tree is like:-
#             10
#         20       30
#     30      50  60  70
b = BinTree(10)
b.insert_left(20, 10)
b.insert_right(30, 10)
b.insert_left(30, 20)
b.insert_right(50, 20)
b.insert_left(60, 30)
b.insert_right(70, 30)
print(b.arr)