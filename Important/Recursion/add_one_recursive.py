def add_one(arr):
    if arr == [9]:
        return [1,0]
    if arr[-1] < 9:
        arr[-1] += 1
    else:
        arr = add_one(arr[:-1]) + [0]
    return arr

# A helper function for Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")    
    
# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

def add_one(arr):
    if arr == [9]:
        return [1,0]
    if arr[-1] < 9:
        arr[-1] = arr[-1]+1
    else:
        arr = add_one(arr[:-1]) + [0]
    return arr

arr = [1,0,9]
print(add_one(arr))

# print first n using recursion
def pprint(n,i):
    if i > n:
        return
    print(i)
    pprint(n, i+1)

print("**pRINT n natural")
pprint(5,1)
def bprint(n,i):
    if i == 0:
        return
    bprint(n, i-1)
    print(i)
print("BACKTRACKING")
bprint(5,5)