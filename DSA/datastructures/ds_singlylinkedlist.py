class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
class SLL:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def insert_at_start(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n
        self.length += 1
    
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data)
            self.length += 1
            return
        x = self.head
        while x.next:
            x = x.next
        x.next = Node(data)
        self.length += 1

    def delete_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        x = self.head
        while x:
            if x.next.data == data:
                x.next = x.next.next
                break
            x = x.next
        self.length -= 1
    # def print_sll(self):
    #     x = self.head
    #     while x:
    #         print(x.data)
    #         x = x.next
    
        
# s = SLL()
# s.insert_at_start(1)
# s.insert_at_start(2)
# s.insert_at_start(3)
# s.insert_at_end(0)
# s.insert_at_end(-1)
# print(s.head)
# s.delete_node(1)
# print(s.head)
# s.delete_node(3)
# print(s.head)
# print(s.length)
