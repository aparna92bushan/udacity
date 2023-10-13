class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    first_node = Node(value)
    first_node.next = self.head
    self.head = first_node


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend
# # Test prepend
# linked_list = LinkedList()
# linked_list.prepend(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here
    if not self.head:
        self.head = Node(value)
        return
    curr_node = self.head
    while curr_node.next:
        curr_node = curr_node.next
    curr_node.next = Node(value)

LinkedList.append = append
def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    curr_node = self.head
    while curr_node:
        if curr_node.value == value:
            return curr_node
        else:
            curr_node = curr_node.next

LinkedList.search = search
def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    if self.head.value == value:
        self.head = self.head.next
        return
    curr_node = self.head
    while curr_node.next:
        if curr_node.next.value == value:
            curr_node.next = curr_node.next.next
            return
        curr_node = curr_node.next

LinkedList.remove = remove

def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if not self.head:
        return None
    node = self.head
    self.head = self.head.next
    return node.value

LinkedList.pop = pop

def length(self):
    l = 0
    cur_node = self.head
    while cur_node:
        l += 1
        cur_node = cur_node.next
    return l
LinkedList.length = length

def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """

    if pos == 1 or not self.head:
        node = Node(value)
        node.next = self.head
        self.head = node
        return
    l = self.length()
    if pos > l-1:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(value)
        return
    counter = 1
    cur_node = self.head
    while cur_node:
        if counter + 1 == pos:
            node = Node(value)
            node.next = cur_node.next
            cur_node.next = node
            return
        cur_node = cur_node.next
        counter += 1
LinkedList.insert = insert
# # Test append - 1
# linked_list = LinkedList()
# linked_list.prepend(1)
# linked_list.append(3)
# linked_list.prepend(2)
# assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
# linked_list = LinkedList()
# linked_list.append(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
# linked_list.append(3)
# assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
# linked_list = LinkedList()
# linked_list.prepend(2)
# linked_list.prepend(1)
# linked_list.append(4)
# linked_list.append(3)
# assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
# assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

linked_list = LinkedList()
# linked_list.prepend(2)
# linked_list.prepend(1)
# linked_list.append(1)
# linked_list.append(3)
# linked_list.append(4)
# linked_list.append(3)

# Test remove
# linked_list.remove(1)
# assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
# linked_list.remove(3)
# assert linked_list.to_list() == [2, 1, 4, 0], f"list contents: {linked_list.to_list()}"

# Test pop
# print(linked_list.to_list())
# value = linked_list.pop()
# print(linked_list.to_list())
# assert value == 1, f"list contents: {linked_list.to_list()}"
# assert linked_list.head.value == 2, f"list contents: {linked_list.to_list()}"

print(linked_list.to_list())
linked_list.insert(10, 1)

print(linked_list.to_list())