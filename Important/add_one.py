# Problem Statement
# You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

# Example 1:

# input = [1, 2, 3]
# output = [1, 2, 4]
# Example 2:

# input = [1, 2, 9]
# # output = [1, 3, 0]
# Challenge: One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.

# But can you solve it in some other way?

# Exercise - Write your function definition here.
# Note - Try proposing a non-recursive solution. We will see a recursive solution in the next lesson "Recursion".

# def add_one(arr):
#     """
#     :param: arr - list of digits representing some number x
#     return a list with digits represengint (x + 1)
#     """
#     carry = 1
#     for i in range(len(arr), 0, -1):
#         if arr[i-1] < 9:
#             arr[i-1] = arr[i-1] + carry
#             carry = 0
#         else:
#             arr[i-1] = 0
#             carry = 1
#         if carry == 0:
#             break
#     if carry:
#         arr.insert(0,carry)
#     return arr

def add_one(arr):
    carry = 1
    for i in range(len(arr),0, -1):
        digit = arr[i-1]+carry
        carry = digit //10
        if carry == 0:
            arr[len(arr)-1] = digit
            break
        else:
            arr[i-1] = digit % 10
    if carry:
        arr = [carry] + arr
    return arr
# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")
# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 9, 8]
solution = [1, 9, 9]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)