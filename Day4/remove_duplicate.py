arr = [0, 0, 1, 1, 1, 2, 2, 3, 4, 4, 5]

def remove_duplicate(arr):
    left_pointer = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[left_pointer] = arr[i]
            left_pointer += 1

    return left_pointer

