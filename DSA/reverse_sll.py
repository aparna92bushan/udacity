# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from datastructures.ds_singlylinkedlist import SLL

class Solution:
    #1. Iterative method:- 
    # The idea is to use three pointers curr, prev, and next to keep track of nodes to update reverse links.
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
s = SLL()
s.insert_at_end(1)
s.insert_at_end(2)
s.insert_at_end(3)
s.insert_at_end(4)
print(s.head)

sol = Solution()
reversed_sll = sol.reverseList(s.head)
print(reversed_sll)

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         new_list_head = None
#         current = head

#         while current:
#             next_node = current.next
#             current.next = new_list_head
#             new_list_head = current
#             current = next_node
#         return new_list_head
    
    # 1 -> 2 -> 3 -> 4
    # c    n
    #      c      n
    #             c   n
    #                 c   n->None

    

    # 4       ->      3       ->        2       ->   1       ->  None
    # new_list