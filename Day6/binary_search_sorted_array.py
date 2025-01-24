arr = [7, 5, 1, 3, 9, 5]
arr.sort()  # O(n log n) time complexity
target = 5

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            mid = left + 1
        else:
            mid = right - 1

    return 0

print(binary_search(arr, target))
