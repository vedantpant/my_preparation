# Given an array of integers nums and an integer k,
# return the total number of contiguous subarrays whose sum equals k.
from collections import defaultdict

nums = [1, 1, 1]
k = 2

def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = defaultdict(int)
    prefix_map[0] = 1

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] += count

    return count

print(subarray_sum(nums, k))
