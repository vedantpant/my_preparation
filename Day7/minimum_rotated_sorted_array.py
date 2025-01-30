nums = [3, 4, 5, 1, 2]


def findmin_sortedArray(nums):
    result = nums[0]
    left = 0
    right = len(nums) - 1

    while left <= right:
        # if array is sorted
        if nums[left] < nums[right]:
            result = min(result, nums[left])
            break

        mid = (left + right) // 2
        result = min(result, nums[mid])
        # if left half is sorted
        if nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return result


print(findmin_sortedArray(nums))
