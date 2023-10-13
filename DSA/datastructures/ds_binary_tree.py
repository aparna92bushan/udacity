# implementation two ways:-
# 1. Linked structure:- 
#     data , left , right 
#     or
#     data, left, right, parent
# 2. Array based:-
#     This is based on BFS traversal i,e level order. 
#     if root is at arr[0], then 
#         left child index    = 2*0 + 1
#         right child index   = 2*0 + 2

#         so 2*n + 1  and 2*n + 2 are the children of a node at position n 

class Node:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None
    
def preorder(root):
    # root left right
    # if self
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    # left root right
    if not root:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
    
def postorder(root):
    # left right root
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")

n = Node(10)
n.left = Node(20)
n.right = Node(30)
n.left.left = Node(30)
n.left.right = Node(50)
n.right.left = Node(60)
n.right.right = Node(70)

print("inorder ", inorder(n))
print("preorder ", preorder(n))
print("postorder ", postorder(n))

# say the tree is like:-
#             10
#         20       30
#     30      50  60  70
