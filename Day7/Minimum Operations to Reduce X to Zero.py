nums = [1, 1, 4, 2, 3]
x = 5

def minOperation(nums, x):
    target = sum(nums) - x

    if target < 0: return -1

    left, curr_sum, max_len = 0, 0, -1
    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum > target and left <= right:
            curr_sum -= nums[left]
            left += 1

        if curr_sum == target:
            max_len = max(max_len, right- left+ 1)

    return len(nums) - max_len if max_len != -1 else -1

print(minOperation(nums, x))