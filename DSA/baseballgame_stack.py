# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, 
# you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record 
# and is one of the following:

# 1.An integer X.
# Record a new score of x.
# 2. '+'.
# Record a new score that is the sum of the previous two scores.
# 3. 'D'.
# Record a new score that is the double of the previous score.
# 4. 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer 
# and that all operations are valid.
# Input: ops = ["5","2","C","D","+"]
# Output: 27

class Solution:
    def baseballscore(self, arr):
        s = []
        # Python 3.10 has match case like switch case in Java
        for op in arr:
            match op:
                case '+':
                    s.append(s[-1]+s[-2])
                case 'D':
                    s.append(2*s[-1])
                case 'C':
                    s.pop()
                case default:
                    s.append(int(op))
        return sum(s)
    
s = Solution()
ops = ["5","2","C","D","+"]
print(s.baseballscore(ops))