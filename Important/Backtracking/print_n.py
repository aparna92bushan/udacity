def print1_n(n,i):
    if i < 1:
        return
    else:
        print1_n(n, i-1)
        print(i)

# print1_n(3,3)

def print1_n(n,i):
    if i > n:
        return
    else:
        print1_n(n, i+1)
        print(i)
print1_n(4,1)