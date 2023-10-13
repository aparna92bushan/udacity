class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def even_after_odd(head):
    if not head:
        return None
    even_head = None
    odd_head = None
    cur_node = head
    even_head_actual = None
    odd_head_actual = None
    while cur_node:
        if cur_node.data % 2 == 0:
            if not even_head:
                even_head = cur_node
                even_head_actual = even_head
            else:
                even_head.next = cur_node
                even_head = even_head.next
        else:
            if not odd_head:
                odd_head = cur_node
                odd_head_actual = odd_head
            else:
                odd_head.next = cur_node
                odd_head = odd_head.next
        cur_node = cur_node.next
    if not odd_head:
        return even_head_actual
    odd_head.next = even_head_actual
    return odd_head_actual

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

# ll_head = create_linked_list([1,2,3,4,5,6])
def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()
# print_linked_list(ll_head)

# hh = even_after_odd(head) 
# print_linked_list(hh)
def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]
    
    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)    
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")            
    except Exception as e:
        print("Fail")
arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
print_linked_list(head)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)