def create_pascal(n):
#     1
#     1 1
#     1 2 1
#     1 3 3 1
#     1 4 6 4 1
#     1 5 10 10 1
    # logic is every ith element in ith row is sum of ith element and i-1 element from previous row.
    cur_row = [1]
    if  n == 1:
        return [1]
    for i in range(1, n+1):
        prev_row = cur_row

        cur_row = [1]
        for j in range(1, i):
            next_num = prev_row[j] + prev_row[j-1]
            cur_row.append(next_num)
        cur_row.append(1)
    return cur_row







# def nth_row_pascal(n):
#     """
#     :param: - n - index (0 based)
#     return - list() representing nth row of Pascal's triangle
#     """
# #     1
# #     1 1
# #     1 2 1
# #     1 3 3 1
# #     1 4 6 4 1
# #     1 5 10 10 1
#     if n == 0:
#         return [1]
#     curr_row = [1]
#     for i in range(1, n+1):
#         prev_row = curr_row
#         curr_row = [1]
#         for j in range(1, i):
#             next_num = prev_row[j]+prev_row[j-1]
#             curr_row.append(next_num)
#         curr_row.append(1)
#     return curr_row
# def test_function(test_case):
#     n = test_case[0]
#     solution = test_case[1]
#     output = nth_row_pascal(n)
#     if solution == output:
#         print("Pass")
#     else:
#         print("Fail")
# n = 0
# solution = [1]

# test_case = [n, solution]
# test_function(test_case)

# n = 1
# solution = [1, 1]

# test_case = [n, solution]
# test_function(test_case)

# n = 2
# solution = [1, 2, 1]

# test_case = [n, solution]
# test_function(test_case)

# n = 3
# solution = [1, 3, 3, 1]

# test_case = [n, solution]
# test_function(test_case)

# n = 4
# solution = [1, 4, 6, 4, 1]

# test_case = [n, solution]
# test_function(test_case)