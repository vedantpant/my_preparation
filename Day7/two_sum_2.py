nums = [1 ,3, 4, 5, 7, 10, 11]
target = 9

def two_sum2(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return [nums[left], nums[right]]
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1


print(two_sum2(nums, target))