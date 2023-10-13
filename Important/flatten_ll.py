# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# User defined class
class Node:
    def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None
    
    # def __repr__(self):
    #     return str(self.value)
    
# User defined class
class LinkedList: 
    def __init__(self): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = None
    
    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def __iter__(self):
        cur_node = self.head
        while cur_node:
            if isinstance(cur_node, LinkedList):
                child_h = cur_node.head
                while child_h:
                    yield child_h.value
                    child_h = child_h.next
            if isinstance(cur_node, Node):
                yield cur_node.value
            cur_node = cur_node.next
            

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

        
    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object
        
        while node:     # <-- Iterate untill we have nodes available
            if isinstance(node.value, LinkedList):
                out.extend(list(node.value)) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            if isinstance(node.value, Node):
                out.append(node.value)
                # needs to have normal int instance logic as well
            node = node.next
        
        return out
def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    list3 = LinkedList()
    node1 = list1.head if list1.head else None
    node2 = list2.head if list2.head else None
    
    while node1 and node2:
        if node1.value < node2.value:
            list3.append(node1.value)
            node1 = node1.next
        else:
            list3.append(node2.value)
            node2 = node2.next
    if node1:
        while node1:
            list3.append(node1.value)
            node1 = node1.next
    if node2:
        while node2:
            list3.append(node2.value)
            node2 = node2.next
    
    return list3
class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
        list3 = LinkedList() 
        cur_node = self.head
        while cur_node:
            list3 = merge(list3, cur_node.value)
            cur_node = cur_node.next
        return list3
l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)

l2 = LinkedList()
l2.append(4)
l2.append(5)
l2.append(6)

l3 = merge(l1, l2)
print(list(l3))
nest = NestedLinkedList()
nest.append(l1)
nest.append(l2)

flat = nest.flatten()