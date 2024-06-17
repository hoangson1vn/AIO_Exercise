def max_kernel(num_list, k):
    result = []
    i = 0
    j = k
    while i < len(num_list) and j <= len(num_list):
        result.append(max(num_list[i:j]))
        i += 1
        j += 1
    return result


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
