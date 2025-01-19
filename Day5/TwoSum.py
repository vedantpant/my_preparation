arr1 = [1, -2, 1, 0, 5]
target = 0

def two_sum(arr1, target):
    i, j = 0, 0
    n = len(arr1)
    for i in range(0, n):
        for j in range(i+1, n):
            if arr1[i] + arr1[j] == target:
                return True

    return False


print(two_sum(arr1, target))
