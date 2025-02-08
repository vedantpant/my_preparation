arr1 = [1, 2, 3, 4]
arr2 = [2, 4, 6, 7, 8]

def intersection_two_array(arr1, arr2):
    result = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            result.append(arr1[i])
            i += 1
            j += 1

    return result

print(intersection_two_array(arr1, arr2))  # Output: [2, 4]