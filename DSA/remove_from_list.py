class Solution:
    def remove(self, arr, val):
        for i in range(0, len(arr)):
            if arr[i] == val:
                t = arr[i]
                del arr[i]
                return t

x = [1,2,3,4,5,5]
s = Solution()
print(s.remove(x, 5))
print(x)