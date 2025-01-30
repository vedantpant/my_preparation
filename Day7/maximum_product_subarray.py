nums = [2, 3, -2, 4]
target = 6

def max_prod_subarray(nums, target):
    res = max(nums)
    currMin, currMax = 1, 1

    for num in nums:
        if num == 0:
            currMin, currMax = 1, 1
            continue
        temp = currMax * num
        currMax = max(num * currMax, num * currMin, num)
        currMin = min(temp, num * currMin, num)
        res = max(res, currMax)

    return res


print(max_prod_subarray(nums, target))
