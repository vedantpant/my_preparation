arr = [1,2,2,1,1,3]

def unique_occurrences(arr):

    freq_count = {}

    for num in arr:
        if num in freq_count:
            freq_count[num] += 1
        else:
            freq_count[num] = 1

    freq_values = list(freq_count.values())
    return len(freq_values) == len(set(freq_values))


print(unique_occurrences(arr))