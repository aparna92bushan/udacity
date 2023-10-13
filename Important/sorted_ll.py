# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
class SortedLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        
        # TODO: Write your sorted append function here
        if not self.head:
            self.head = Node(value)
            return
        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return
        node = self.head
        while node.next is not None and value > node.next.value:
            node = node.next
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node
        
# # Test cases
# linked_list = SortedLinkedList()
# linked_list.append(3)
# print ("Pass" if (linked_list.head.value == 3) else "Fail")

# linked_list.append(2)
# print ("Pass" if (linked_list.head.value == 2) else "Fail")

# linked_list.append(4)
# node = linked_list.head.next.next
# print ("Pass" if (node.value == 4) else "Fail")

def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    
    # TODO: Write your sorting function here
    sorted_ll = SortedLinkedList()
    for element in array:
        sorted_ll.append(element)
    sorted_array = []
    cur_node = sorted_ll.head
    while cur_node:
        sorted_array.append(cur_node.value)
        cur_node = cur_node.next
    return sorted_array
x = sort([4, 8, 2, 1, -3, 1, 5])
print(x)
# Test case
print ("Pass" if (sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")