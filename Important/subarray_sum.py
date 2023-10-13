# Given an integer array, check if it contains a subarray having zero-sum.

# For example,

# Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
 
# Output: Subarray with zero-sum exists
 
# The subarrays with a sum of 0 are:
 
# { 3, 4, -7 }
# { 4, -7, 3 }
# { -7, 3, 1, 3 }
# { 3, 1, -4 }
# { 3, 1, 3, 1, -4, -2, -2 }
# { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
# Note that the problem deals with subarrays that are contiguous, i.e., whose elements occupy consecutive positions in the array.

def subarray_sum(arr):
    subarrays = []
    if sum(arr) == 0:
        subarrays.append(arr)
    for i in range(0, len(arr)):
        num = arr[i]
        for j in range(i+1, len(arr)):
            num += arr[j]
            if num == 0:
                subarrays.append(arr[i:j+1])
                break
    print(subarrays)

arr = [ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 ]
subarray_sum(arr)