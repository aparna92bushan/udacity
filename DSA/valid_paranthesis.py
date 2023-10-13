# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s):
        map = {")":"(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in map: #Takes care of normal chars as well
                stack.append(c)
                continue
            if stack and stack[-1] != map[c]:
                return False
            stack.pop()
        return not stack

# class Solution:
#     def isValid(self, s):
#         stack = []
#         flag = 0
#         try:
#             for e in s:
#                 if e in (["(", "{", "["]):
#                     stack.append(e)
#                 elif e == ")":
#                     e_top = stack.pop()
#                     if e_top != "(":
#                         return False
#                     else:
#                         flag = 1
#                         continue
#                 elif e == "}":
#                     e_top = stack.pop()
#                     if e_top != "{":
#                         return False
#                     else: 
#                         flag = 1
#                         continue
#                 elif e == ']':
#                     e_top = stack.pop()
#                     if e_top != '[':
#                         return False
#                     else:
#                         flag = 1
#                         continue
#             return True if flag == 1 and len(stack)==0 else False
#         except Exception as e:
#             return False

sol = Solution()
# input_str = "(){[]}"
# input_str = "([]){"
input_str = "]"
# input_str = "bbmnxbvjs"
print(sol.isValid(input_str))