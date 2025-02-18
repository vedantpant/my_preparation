nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# def max_subarray(nums):
#     max_sub = nums[0]
#     current_sum = 0
#
#     for n in nums:
#         if current_sum < 0:
#             current_sum = 0
#         current_sum += n
#         max_sub = max(max_sub, current_sum)
#     return max_sub

def max_subarray(nums):
    max_sub = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += n
        max_sub = max(max_sub, current_sum)
    return max_sub

print(max_subarray(nums))




