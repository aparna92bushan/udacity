# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
# class LinkedList:
#     def __init__(self, init_list=None):
#         self.head = None
#         if init_list:
#             for value in init_list:
#                 self.append(value)
        
#     def append(self, value):
#         if self.head is None:
#             self.head = Node(value)
#             return
        
#         # Move to the tail (the last node)
#         node = self.head
#         while node.next:
#             node = node.next
        
#         node.next = Node(value)
#         return


# def iscircular(linked_list):
#     """
#     Determine whether the Linked List is circular or not

#     Args:
#        linked_list(obj): Linked List to be checked
#     Returns:
#        bool: Return True if the linked list is circular, return False otherwise
#     """
    
#     # TODO: Write function to check if linked list is circular
# #     We use fast and slow pointer pattern to solve it. if both pointers meet, means there is a loop, otherwise fast will rach the end of the list early and we stop there.
#     slow = fast = linked_list.head
#     while slow and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             return True
#     return False
# # Create another circular linked list
# small_loop = LinkedList([0])
# small_loop.head.next = small_loop.head

# list_with_loop = LinkedList([2, -1, 3, 0, 5])

# # Creating a loop where the last node points back to the second node
# loop_start = list_with_loop.head.next

# node = list_with_loop.head
# while node.next: 
#     node = node.next   
# node.next = loop_start
# print ("Pass" if iscircular(list_with_loop) else "Fail")                  # Pass
# print ("Pass" if iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")   # Fail
# print ("Pass" if iscircular(LinkedList([1])) else "Fail")                 # Fail
# print ("Pass" if iscircular(small_loop) else "Fail")                      # Pass
# print ("Pass" if iscircular(LinkedList([])) else "Fail")                  # Fail

def test_yield():
    for i in range(0, 10):
        yield i
# t = test_yield()
for ele in test_yield():
    print(ele)
# tn = next(t)
# while tn is not None:
#     print(tn)
#     tn = next(t)