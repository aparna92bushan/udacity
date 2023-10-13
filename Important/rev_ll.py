from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self) -> str:
        return str(list(self))
    # def __repr__(self):
    #     return str([v for v in self])
# def reverse(linked_list):
#     """
#     Reverse the inputted linked list

#     Args:
#        linked_list(obj): Linked List to be reversed
#     Returns:
#        obj: Reveresed Linked List
#     """
    
#     # TODO: Write your function to reverse linked lists here
#     cur_node = linked_list.head
#     rev_list = LinkedList()
#     stack = deque()
#     while cur_node.next:
#         stack.appendleft(cur_node)
#         cur_node = cur_node.next
#     rev_list.append(cur_node.value)

#     while stack:
#         rev_list.append(stack.popleft().value)
    
#     return rev_list
def reverse(linked_list):
    prev = None
    new_list = LinkedList()
    for ele in linked_list:
        new_node = Node(ele)
        new_node.next = prev
        prev = new_node
    new_list.head = prev
    return new_list
llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)
print(llist)
print("original", list(llist))
flipped = reverse(llist)
print("flipped", list(flipped))
# is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
# print("Pass" if is_correct else "Fail")
    