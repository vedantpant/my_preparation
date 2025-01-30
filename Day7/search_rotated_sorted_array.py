# rotate array
nums = [4, 5, 6, 7, 0, 1, 2]
k = 3
target = 0


# def rotate_array_right(nums, k):
#     k = k % len(nums)
#     nums = nums[::-1]
#     nums[:k] = reversed(nums[:k])
#     nums[k:] = reversed(nums[k:])
#
#     return nums
#
#
# print(rotate_array_right(nums, k))

# def rotate_array_left(nums, k):
#     k = k % len(nums)
#     nums[:k] = reversed(nums[:k])
#     nums[k:] = reversed(nums[k:])
#     nums[:] = reversed(nums[:])
#
#
#     return nums
#
# print(rotate_array_left(nums, k))

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        # right sorted portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


print(search(nums, target))




