def is_pallindrome(str):
    if len(str) == 0:
        return False
    if len(str) == 1:
        return True
    if str[0] != str[-1]:
        return False
    return str[0] == str[-1] and is_pallindrome(str[1:-1])

str = ""
print(is_pallindrome(str))