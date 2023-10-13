def reverse_string(input, n):
    if n < 1:
        return ""
    if n == 1:
        return input[0]
    print(n)
    return input[n-1] + reverse_string(input, n-1)
# Test Cases

print(reverse_string("abc", 3))
# print ("Pass" if  ("" == reverse_string("", 0)) else "Fail")
# print ("Pass" if  ("cba" == reverse_string("abc", 3)) else "Fail")