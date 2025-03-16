arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]

def find_special_integer(arr):
    n = len(arr)
    step = n // 4
    for i in range(n - step):
        if arr[i] == arr[i + step]:
            return arr[i]

print(find_special_integer(arr))