# find nth fibonacci number
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        l1 = fibonacci(n-1) 
        l2 = fibonacci(n-2)
        return l1+l2
    
print(fibonacci(5))
# looks like - tc = 2^n We can reduce it by dynamic programming