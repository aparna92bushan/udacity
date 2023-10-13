def reverse(str, n):
    if n < 0:
        return ""
    else:
        return str[n]+ reverse(str, n-1)
    
# rev = reverse("aparna", 5)
# print(rev, len(rev))
import time
def reverse_array(arr):
    if len(arr) == 1:
        return arr
    else:
        return [arr[-1]] + reverse_array(arr[:-1])

arr = [1,2,3,4,5]
t1=time.time()
print(reverse_array(arr))
t2 = time.time()
# let's try to reverse using 2 pointers. swap left and right elements in array
print("************")
def reverse_array(arr, l, r):
    if l >= r:
        return []
    else:
        arr[l], arr[r] = arr[r], arr[l]
        reverse_array(arr, l+1, r-1)
        return arr

arr = [1,2,3,4,5]
t3=time.time()
print(reverse_array(arr, 0, 3))
t4 = time.time()

print((t2-t1)/(t4-t3))

def is_pallindrome(str, l, r):
    if l > r:
        return True
    if str[l] != str[r]:
        return False
    return is_pallindrome(str, l+1, r-1)

str = "madams"
print("Given string is pallindrome: ",is_pallindrome(str, 0, len(str)-1))
    