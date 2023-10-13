
def summation(n, i):
    if i > n:
        return 0
    else:
        return i + summation(n, i+1)
    
print("sum1", summation(4,1))

def factorial(n, i):
    if i > n:
        return 1
    else:
        return i * factorial(n, i+1)
    
print(factorial(4,1))

def sum2(sum, i):
    if i < 1:
        print(sum)
        return
    else:
        return sum2(sum+i, i-1)
sum2(0, 5)

