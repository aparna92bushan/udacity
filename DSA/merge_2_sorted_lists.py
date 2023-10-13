# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Algorithm
# 1. Create dummy head. We return dummy head's next
# 2. Create a prev variable and set it to dummy head. will use this to build out o/p list
# 3. l1 points to list1 head, l2 points to list2 head
# 4. Compare l1 and l2 , update prev.next to either l1 or l2 whichever is smaller. l1 breaks the tie
#     update prev
# 5. if either l1 or l2 runout set prev.next to the rest of the other lst

from datastructures.ds_singlylinkedlist import SLL

class Solution:
    def merge_lls(self, l1, l2):
        dummy = SLL()
        prev = dummy
        while l1 and l2:
            if l1.data <= l2.data:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2
        return dummy.next

l1 = SLL()
l1.insert_at_end(1)
l1.insert_at_end(2)
l1.insert_at_end(4)

l2 = SLL()
l2.insert_at_end(1)
l2.insert_at_end(3)
l2.insert_at_end(4)
l2.insert_at_end(6)

s = Solution()
print(s.merge_lls(l1.head,l2.head))

l3 = SLL()
l4 = SLL()
l4.insert_at_end(1)
print(s.merge_lls(l3.head, l4.head))