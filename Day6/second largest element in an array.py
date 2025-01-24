arr = [7, 5, 1, 3, 9, 5]

def find_second_largest(arr):
    n = len(arr)

    if n < 2:
        return "atleast more than 2 elements."

    largest = second = 0

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

print(find_second_largest(arr))