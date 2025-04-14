nums = [2,3,1,2,4,3]
target = 7

def min_sub_array(nums, target):
    total = 0
    min_len = float("inf")
    left = 0

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0

print(min_sub_array(nums, target))

