arr = [1, 5, 7, 1, 5, 3, 3, 9, 7]
k = 8

def find_max_pair_k(arr, k):
    freq = {}
    count = 0
    list_pair = []
    for num in arr:
        complement = k - num
        if complement in freq and freq[complement] > 0:
            count += 1
            list_pair.append((num, complement))
            freq[complement] -= 1
        else:
            freq[num] = freq.get(num, 0) + 1

    return count, list_pair

print(find_max_pair_k(arr, k))