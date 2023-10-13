# Given an integer array nums of length n, you want to create an array ans of length 2n 
# where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

class Solution:
    def concatenate(self, arr1):
        l = len(arr1)
        a2 = []
        for i in range(2*l):
            a2.append(arr1[i%l])
        return a2
        # a2 = []
        # for i in range(2):
        #     for a in arr1:
        #         a2.append(a)
        # return a2
    
a1 = [1,2,34]

s = Solution()
print(s.concatenate(a1))