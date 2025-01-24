arr = [7, 5, 1, 3, 9, 5]
target = 14

def two_sum(arr, target):
    n = len(arr)
    for i in range(0, n):
        for j in range(1, n):
            if arr[i] + arr[j] == target:
                return True

    return False


print(two_sum(arr, target))