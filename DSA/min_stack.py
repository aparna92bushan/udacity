# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
class Minstack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            mn = min(self.stack[-1][1], val)
            self.stack.append((val, mn))

    def pop(self):
        if not self.stack:
            raise IndexError("Can't pop from empty list")
        top = self.stack[-1][0]
        self.stack.pop()
        return top

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return None
    # def __init__(self):
    #     self.stack = []
    #     self.min = [] #list because we can have duplicate elements

    # def push(self, val):
    #     self.stack.append(val)
    #     if not self.min or self.min[-1] >= val:
    #         self.min.append(val)

    # def pop(self):
    #     if not self.stack:
    #         raise IndexError("Can't pop from empty list")
    #     if self.min[-1] == self.stack.pop():
    #         self.min.pop()

    # def top(self):
    #     if self.stack:
    #         return self.stack[-1]

    # def getMin(self):
    #     if self.min:
    #         return self.min[-1]
    #     return None

ms = Minstack()
ms.push(1)
ms.push(-1)
ms.push(10)
print(ms.min)
print(ms.top())
print(ms.getMin())
ms.pop()
print(ms.stack)