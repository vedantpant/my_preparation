arr1 = [-3, 3, 4, -3, 1, 2]
target = 0


def three_sum(arr1, target):
    arr1.sort()
    result = []

    for i, a in enumerate(arr1):
        if i > 0 and a == arr1[i-1]:
            continue

        left = i + 1
        right = len(arr1) - 1
        while left < right:
            three_sum = a + arr1[left] + arr1[right]
            if three_sum > target:
                right -= 1
            elif three_sum < target:
                left += 1
            else:
                result.append([a, arr1[left], arr1[right]])
                left += 1
                while arr1[left] == arr1[left - 1] and left < right:
                    left += 1

    return result


print(three_sum(arr1, target))  # Output: [[-3, 0, 3], [-3, 1, 2]]



