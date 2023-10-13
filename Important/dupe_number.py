# Problem Statement
# You have been given an array of length = n. The array contains integers from 0 to n - 2. Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array

# Example:

# arr = [0, 2, 3, 1, 4, 5, 3]
# output = 3 (because 3 is present twice)
# The expected time complexity for this problem is O(n) and the expected space-complexity is O(1).

# def duplicate_number(arr):
#     """
#     :param - array containing numbers in the range [0, len(arr) - 2]
#     return - the number that is duplicate in the arr
#     """
#     arr.sort()
#     for i in range(0, len(arr)):
#         if arr[i] == arr[i+1]:
#             return arr[i]
def duplicate_number(arr):
#     Sum of n natural numbers is n(n+1)/2 , we can use this clue
    l = len(arr)
    expected_sum = (l-2)*(l-2+1)/2
    sum = 0
    for num in arr:
        sum += num
    return sum-expected_sum
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)
arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)
arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)
arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5

test_case = [arr, solution]
test_function(test_case)