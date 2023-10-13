def print_n(n, i):
    if i>n:
        return
    else:
        print(i)
        print_n(n, i+1)

print_n(7,1)
print("*********")
def print_n_o(n,i):
    if i < 1:
        return
    else:
        print(i)
        print_n_o(n, i-1)

print_n_o(8, 8)
