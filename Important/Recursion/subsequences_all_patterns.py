# Print all subsequences with given sum
def sub_with_sum(input, i, subarr, given_sum):
    if i>= len(input):
        if sum(subarr) == given_sum:
            print(subarr)
        return
    subarr.append(input[i])
    sub_with_sum(input, i+1, subarr, given_sum)
    subarr.pop()
    sub_with_sum(input, i+1, subarr, given_sum)

input = [3,1,2, 0]
s = 2
sub_with_sum(input, 0, [], s)
print("********")
# print any sub sequence with given sum
def one_sub_with_sum(input, i, subarr, given_sum):
    if i >= len(input):
        if sum(subarr) == given_sum:
            return subarr
        return
    subarr.append(input[i])
    arr = one_sub_with_sum(input, i+1, subarr, given_sum)
    if arr:
        return arr
    subarr.pop()
    arr = one_sub_with_sum(input, i+1, subarr, given_sum)
    if arr:
        return arr

input = [3,1,2,0]
s = 2
print(one_sub_with_sum(input, 0, [], s))
# Count the number of subsequences whose sum is given sum

print("********")
def count_sequences_with_given_sum(input, i, subarr, given_sum):
    if i >= len(input):
        if sum(subarr) == given_sum:
            print(subarr)
            return 1
        return 0
    subarr.append(input[i])
    l = count_sequences_with_given_sum(input, i+1, subarr, given_sum)
    subarr.pop()
    r =  count_sequences_with_given_sum(input, i+1, subarr, given_sum)
    return l+r
input = [3,1,2,0,-1]
given_sum = 2
print(count_sequences_with_given_sum(input, 0, [], given_sum))