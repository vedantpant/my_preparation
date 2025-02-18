nums = [1,2,3,4,5,6,7,8,3]

def find_peak_element(nums):
    n = len(nums)

    for i in range(n):
        left = True
        right = True
        # check left elements
        if i > 0 and nums[i] <= nums[i - 1]:
            left = False

        if i < n - 1 and nums[i] <= nums[i + 1]:
            right = False
            
        if left and right:
            return i


print(find_peak_element(nums))

