arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]

def merge_array(arr1,arr2):
    merged_arr = arr1 + arr2
    merged_arr.sort()
    return merged_arr

print(merge_array(arr1, arr2))