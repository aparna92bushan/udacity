class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
# Root left right
# say the tree is like:-
#             10
#         20       30
#     30      50  60  70

#   10 20 30 50 30 60 70
    # print(root)
    # preorder(root.left)
    # preorder(root.right)
    curr, stack = root, []
    res = []
    while curr or stack:
        if curr:
            res.append(curr.data)
            stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()
    return res

def inorder(root):
# Left root right
# say the tree is like:-
#             10
#         20       30
#     30      50  60  70

#   30 20 50 10 60 30 70
    curr, stack = root, []
    res = []
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res.append(curr.data)
            curr = curr.right
    return res

def postorder(root):
# Left right root
# say the tree is like:-
#             10
#         20       30
#     30      50  60  70

#   30 50 20 60 70 30 10
    curr, stack =root, []
    res = []
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if temp == None:
                temp = stack.pop()
                res.append(temp.data)
                while stack and (temp == stack[-1].right):
                    temp = stack.pop()
                    res.append(temp.data)
            else:
                curr = temp
    return res

def postorder(root):
    curr, stack = root, []
    res = []
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if not stack:
                break
            curr = stack[-1].right
            if not curr:
                last = None
                while stack and stack[-1].right == last:
                    last = stack.pop()
                    res.append(last.data)
    return res  
# Tree 1
n = Node(10)
n.left = Node(20)
n.right = Node(30)
n.left.left = Node(30)
n.left.right = Node(50)
n.right.left = Node(60)
n.right.right = Node(70)

# Tree 2
# n = Node(20)
# n.left = Node(15)
# n.right = Node(40)
# n.left.left = Node(19)
# n.left.right = Node(12)
# n.left.right.left = Node(11)
# n.left.right.right = Node(13)
# n.left.right.right.left = Node(17)
# n.left.right.right.right = Node(16)

print(postorder(n))

