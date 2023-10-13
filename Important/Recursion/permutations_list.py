ans = []
def permute(input_list, i):
    if i == len(input_list):
        # ans.append(input_list)
        print(input_list)
        return
    for j in range(i, len(input_list)):
        input_list[i], input_list[j] = input_list[j], input_list[i]
        permute(input_list, i+1)
        input_list[i], input_list[j] = input_list[j], input_list[i]

def call_permute(input_list):
    permute(input_list, 0)

input_list = [1,2,3]
call_permute(input_list)
