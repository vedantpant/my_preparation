nums = [10, 5, 2, 6]
k = 100

def subarray_product_less_k(nums,k):
    left, right = 0, 0

    product = 1
    count = 0

    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product /= nums[left]
            left += 1
        count += right - left + 1

    return count



