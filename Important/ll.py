class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    if not input_list:
        return None
    head = Node(input_list[0])
    dupe_head = head
    for i in range(1, len(input_list)):
        if dupe_head:
            node =Node(input_list[i])
            dupe_head.next = node
            dupe_head = dupe_head.next
    return head

def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
#             print(head)
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)
        
ip = [1,2,3]
head = create_linked_list(ip)
test_function(ip, head)

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
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    
    def to_list(self):
        
        # TODO: Write function to turn Linked List into Python List
        current_node = self.head
        converted_list = []
        while current_node:
            converted_list.append(current_node.value)
            current_node = current_node.next
        return converted_list
# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)
print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")

# ###########3 DLL
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        
        # TODO: Implement this method to append to the tail of the list
        if not self.head:
            self.head = self.tail = DoubleNode(value)
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
# Test your class here
linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous
from collections import deque
d = deque()
d.appendleft(1)
d.appendleft(2)
d.pop()