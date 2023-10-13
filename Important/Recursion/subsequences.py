# logic- take or not take element at each index
def subsequence(i, input, arr):
    if i >= len(input):
        print(arr)
        # if len(arr) == 0:
        #     print([])
        return
    arr.append(input[i]) #Take case
    subsequence(i+1, input, arr)
    # print(f"index to be deleted {i} from array {arr}")
    arr.pop()
    subsequence(i+1, input, arr) #not take case

input = [3,1,2]
subsequence(0, input, [])
# TC= 2^n , space = O(n)