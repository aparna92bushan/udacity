# Remove duplicates from a sorted array by updating the array in place, have O(1) space complexity
class Solution:
    def remove_dupes(self, arr):
        # arr = [0,1,1,1, 2,3,4]
        # for i in range(len(arr)-1, 0, -1):
        #     if arr[i] == arr[i-1]:
        #         del arr[i]
        for i in range(1, len(arr)-1):
            if arr[i] == arr[i-1]:
                del arr[i]
    
s = Solution()
a = [0,1,1,1,2,3,4,4]
s.remove_dupes(a)
print(a)
