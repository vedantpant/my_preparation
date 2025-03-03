nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

def rotate_array(nums, k):

    n = len(nums)
    k = k % n

    nums = nums[::-1]

    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    return nums

print(rotate_array(nums, k))