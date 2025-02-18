arr1 = [1, 12, -5, -6 , 50, 3]
k = 4

def max_avg_subarray(arr1, k):
    n = len(arr1)
    window_sum = sum(arr1[:k])
    max_sum = window_sum
    max_index = 0
    for i in range(k, n):
        window_sum += arr1[i] + arr1[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_index = i - k + 1
    return max_index

print(max_avg_subarray(arr1, k))


