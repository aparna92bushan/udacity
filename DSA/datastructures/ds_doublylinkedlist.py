class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    
class DLL():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        
    def insert_at_start(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
            self.tail = n
            self.length += 1
            return
        n.next = self.head
        self.head.prev = n
        self.head = n
        self.length += 1

    def insert_at_end(self, data):
        n = Node(data)
        self.tail.next = n
        n.prev = self.tail
        self.tail = n

        self.length += 1
    
    def delete_node(self, data):
        # Removes first iteration of the data received
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        x = self.head.next
        while x:
            if x.data == data:
                x.prev.next = x.next
                x.next.prev = x.prev
                self.length -= 1
                return

    def delete_at_index(self, index):
        if index >= self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        i = 0
        x = self.head
        while i < index:
            x = x.next
            i += 1
        x.prev.next = x.next
        x.next.prev = x.prev
        self.length -= 1

s = DLL()
s.insert_at_start(1)
print(s.head.prev)
s.insert_at_start(0)
print(s.tail.data)
s.insert_at_start(-1)
s.insert_at_end(7)
print(s.head) #prints from tail towards head , just change print method
# s.delete_node(0)
# print(s.head)
# print("len=",s.length)
# s.delete_node(-1)
# print(s.head)
# print(s.length)
# s.delete_node(7)
# print(s.head)
# print(s.length, s.tail.data)
s.delete_at_index(4)
print(s.head)
print(s.length)
print(s.tail.data)